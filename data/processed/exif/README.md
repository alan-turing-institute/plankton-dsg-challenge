# EXIF data extraction

Each image contains metadata including GPS location where known extracted from the original image.

These data can be extracted to CSV using the following script.

Warning, the disks on the Azure VM are slow, so this takes about 7 hours!

```
cd /data/images
ls | xargs -i exiftool -n -all -csv {} |sort -r | uniq > ~/exif.csv
```
