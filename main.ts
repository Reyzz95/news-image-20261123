// Runner script for news-image-20261123 bounty entry.
// Invokes the Python drawing script to generate entry.png, ensures output directory exists,
// copies it to the output directory, and prints the output path, file size, and success message.

import { copyFileSync, statSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { execSync } from 'node:child_process';

execSync('python3 draw_image.py', { stdio: 'inherit' });

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });

const destPath = join(outDir, 'entry.png');
copyFileSync(new URL('./entry.png', import.meta.url), destPath);

const stats = statSync(destPath);
console.log(`✨ Successfully generated 1024x1024 news collage entry at ${destPath} (${stats.size} bytes)!`);
