# Checklist

- [ ] Are all files non-empty?
- [ ] Did you generate md5sum for `raw` and `processed`?
  - raw: `fd 'fastq.gz' -x md5sum > checksum.md5`
  - processed: `fd '(bam|tsv.gz|mtx.gz)' -x md5sum > checksum.md5`
- [ ] Did you fill in `pipeline.md`?
