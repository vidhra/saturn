# gcloud migration vms image-imports  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports)*

**NAME**

: **gcloud migration vms image-imports - imports images to Google Compute Engine from Google Cloud Storage**

**SYNOPSIS**

: **`gcloud migration vms image-imports` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud alpha migration vms image-imports provides a more robust and better
supported method for importing images to Google Compute Engine. Other
image-related operations (for example, list) can be done using gcloud compute
images, as usual.
The commands use VM Migartion API which supports importing of an image from a
Google Cloud Storage file (gs://…) to a target project. VM Migration API
must be enabled in your project.
gcloud alpha migration vms image-imports create creates an Image Import resource
with a nested Image Import Job resource. The Image Import Job resource tracks
the image import progress. After the Image Import Job completes, successfully or
otherwise, there's no further use for the Image Import resource.
The image is imported to a Google Cloud Project, desginated by the Target
Project resource. To get a list of Target Projects, run the gcloud alpha
migration vms target-projects list command. Use the Google Cloud console to add
target project resources. For information on adding target projects, see [https://cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/target-project](https://cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/target-project).
A project can support a maximum of 1000 Image Import resources per project.
Hence it's recommended to delete an Image Import resource after the Image Import
Job is complete to avoid reaching the Image Import resources limit. Deletion of
Image Import resource does not affect the imported image.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create)`**:
import Virtual Disk images to Google Compute Engine.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/delete)`**:
delete an Image Import resource.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/describe)`**:
describe an Image Import.

**`[list](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/list)`**:
list Image Imports.

**NOTES**

: This variant is also available:

```
gcloud alpha migration vms image-imports
```