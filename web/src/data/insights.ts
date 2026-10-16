import { getCollection, type CollectionEntry } from 'astro:content';

export type Insight = CollectionEntry<'insights'>;

/** Published articles, newest first. */
export async function getInsights(): Promise<Insight[]> {
  const all = await getCollection('insights', ({ data }) => !data.draft);
  return all.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}

export const formatDate = (d: Date) =>
  d.toLocaleDateString('en-ZA', { day: 'numeric', month: 'long', year: 'numeric' });

/** Rough reading time in minutes. */
export const readingTime = (body = '') => Math.max(1, Math.ceil(body.split(/\s+/).length / 200));
