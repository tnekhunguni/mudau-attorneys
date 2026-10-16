// Insights articles: one Markdown file per article in src/content/insights/.
// The file name becomes the address, e.g. ccma-30-days.md -> /insights/ccma-30-days/
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const insights = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/insights' }),
  schema: z.object({
    title: z.string().max(90),
    description: z.string().max(170), // shown in Google results and link previews
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    author: z.string().default('Makondelele Mudau'),
    practice: z.string().optional(), // slug from src/data/practice.ts, links the article to that page
    draft: z.boolean().default(false), // drafts are not published
  }),
});

export const collections = { insights };
