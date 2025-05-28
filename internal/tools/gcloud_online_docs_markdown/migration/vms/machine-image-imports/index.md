# gcloud migration vms machine-image-imports  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports)*

**NAME**

: **gcloud migration vms machine-image-imports - imports machine images to Google Compute Engine from Google Cloud Storage**

**SYNOPSIS**

: **`gcloud migration vms machine-image-imports` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud migration vms machine-image-imports provides a more robust and better
supported method for importing machine images to Google Compute Engine. Other
image-related operations (for example, list) can be done using gcloud compute
images, as usual.
The commands use VM Migration API which supports importing of a machine image
from a Google Cloud Storage file (gs://…) to a target project. VM
Migration API must be enabled in your project.
`gcloud migration vms machine-image-imports create` creates a machine
Image Import resource with a nested Image Import Job resource. The Image Import
Job resource tracks the machine image import progress. After the Image Import
Job completes, successfully or otherwise, there's no further use for the Image
Import resource.
The machine image is imported to a Google Cloud Project, desginated by the
Target Project resource. To get a list of Target Projects, run the gcloud alpha
migration vms target-projects list command. Use the Google Cloud console to add
target project resources. For information on adding target projects, see [https://cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/target-project](https://cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/target-project).
A project can support up to a certain number of Image Import resources per
project. Hence it's recommended to delete an Image Import resource after the
Image Import Job is complete to avoid reaching the Image Import resources limit.
Deletion of Image Import resource does not affect the imported machine image.
For more information about the image import resource, see [https://cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import](https://cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create)`**:
import machine images to Google Compute Engine.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/delete)`**:
delete an Image Import resource.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/describe)`**:
describe an Image Import.

**`[list](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/list)`**:
list Image Imports.

**NOTES**

: This variant is also available:

```
gcloud alpha migration vms machine-image-imports
```