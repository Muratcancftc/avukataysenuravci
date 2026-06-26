import sharp from 'sharp';
import { readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const source = join(root, 'images/logo-emblem.png');
const sizes = [16, 32, 48, 96, 180, 192, 512];

const emblem = await sharp(source).ensureAlpha().toBuffer();
const meta = await sharp(emblem).metadata();
const emblemWidth = meta.width ?? 238;
const emblemHeight = meta.height ?? 161;
const canvas = 512;
const scale = (canvas * 0.82) / Math.max(emblemWidth, emblemHeight);
const resizedWidth = Math.round(emblemWidth * scale);
const resizedHeight = Math.round(emblemHeight * scale);
const left = Math.round((canvas - resizedWidth) / 2);
const top = Math.round((canvas - resizedHeight) / 2);

const emblemResized = await sharp(emblem)
  .resize(resizedWidth, resizedHeight, { fit: 'inside' })
  .toBuffer();

const base = await sharp({
  create: {
    width: canvas,
    height: canvas,
    channels: 4,
    background: { r: 0, g: 0, b: 0, alpha: 1 },
  },
})
  .composite([{ input: emblemResized, left, top }])
  .png()
  .toBuffer();

for (const size of sizes) {
  const out = join(root, size === 180 ? 'favicon-180.png' : `favicon-${size}.png`);
  await sharp(base).resize(size, size).png().toFile(out);
  console.log('wrote', out);
}

await sharp(base).resize(48, 48).png().toFile(join(root, 'favicon.ico'));
console.log('wrote favicon.ico');

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" fill="#000"/>
  <image href="data:image/png;base64,${base.toString('base64')}" width="512" height="512"/>
</svg>
`;
writeFileSync(join(root, 'favicon.svg'), svg);
console.log('wrote favicon.svg');

await sharp(base).resize(512, 512).png().toFile(join(root, 'images/logo-icon-512.png'));
console.log('wrote images/logo-icon-512.png');
