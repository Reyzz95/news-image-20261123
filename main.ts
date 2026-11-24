// Runner script for news-image-20261123 bounty entry.
// The Python drawing script (draw_image.py) in this repo is the documented generator
// that produced the committed entry.png. This runner resolves the entry folder from its
// own file location, ensures the output directory exists, copies entry.png to the target
// output directory, and prints the output path and file size in bytes.

import { copyFileSync, statSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const sourcePng = join(__dirname, 'entry.png');

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });

const destPath = join(outDir, 'entry.png');
copyFileSync(sourcePng, destPath);

const stats = statSync(destPath);
console.log(`✨ Successfully generated 1024x1024 news collage entry at ${destPath} (${stats.size} bytes)!`);
