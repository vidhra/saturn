# medical-imagingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# medical-imaging

## Description

This is the *AWS HealthImaging API Reference* . AWS HealthImaging is a HIPAA eligible service that empowers healthcare providers, life science organizations, and their software partners to store, analyze, and share medical images in the cloud at petabyte scale. For an introduction to the service, see the ` *AWS HealthImaging Developer Guide* [https://docs.aws.amazon.com/healthimaging/latest/devguide/what-is](https://docs.aws.amazon.com/healthimaging/latest/devguide/what-is).html`__ .

### Note

We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see [Tools to build on AWS](http://aws.amazon.com/developer/tools) .

The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the *AWS HealthImaging Developer Guide* where you can view tested code examples.

**Data store actions**

- [CreateDatastore](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_CreateDatastore.html) â See [Creating a data store](https://docs.aws.amazon.com/healthimaging/latest/devguide/create-data-store.html) .
- [GetDatastore](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetDatastore.html) â See [Getting data store properties](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-data-store.html) .
- [ListDatastores](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListDatastores.html) â See [Listing data stores](https://docs.aws.amazon.com/healthimaging/latest/devguide/list-data-stores.html) .
- [DeleteDatastore](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DeleteDatastore.html) â See [Deleting a data store](https://docs.aws.amazon.com/healthimaging/latest/devguide/delete-data-store.html) .

**Import job actions**

- [StartDICOMImportJob](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_StartDICOMImportJob.html) â See [Starting an import job](https://docs.aws.amazon.com/healthimaging/latest/devguide/start-dicom-import-job.html) .
- [GetDICOMImportJob](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetDICOMImportJob.html) â See [Getting import job properties](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-dicom-import-job.html) .
- [ListDICOMImportJobs](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListDICOMImportJobs.html) â See [Listing import jobs](https://docs.aws.amazon.com/healthimaging/latest/devguide/list-dicom-import-jobs.html) .

**Image set access actions**

- [SearchImageSets](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_SearchImageSets.html) â See [Searching image sets](https://docs.aws.amazon.com/healthimaging/latest/devguide/search-image-sets.html) .
- [GetImageSet](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetImageSet.html) â See [Getting image set properties](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-image-set-properties.html) .
- [GetImageSetMetadata](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetImageSetMetadata.html) â See [Getting image set metadata](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-image-set-metadata.html) .
- [GetImageFrame](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetImageFrame.html) â See [Getting image set pixel data](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-image-frame.html) .

**Image set modification actions**

- [ListImageSetVersions](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListImageSetVersions.html) â See [Listing image set versions](https://docs.aws.amazon.com/healthimaging/latest/devguide/list-image-set-versions.html) .
- [UpdateImageSetMetadata](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_UpdateImageSetMetadata.html) â See [Updating image set metadata](https://docs.aws.amazon.com/healthimaging/latest/devguide/update-image-set-metadata.html) .
- [CopyImageSet](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_CopyImageSet.html) â See [Copying an image set](https://docs.aws.amazon.com/healthimaging/latest/devguide/copy-image-set.html) .
- [DeleteImageSet](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DeleteImageSet.html) â See [Deleting an image set](https://docs.aws.amazon.com/healthimaging/latest/devguide/delete-image-set.html) .

**Tagging actions**

- [TagResource](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_TagResource.html) â See [Tagging a resource](https://docs.aws.amazon.com/healthimaging/latest/devguide/tag-resource.html) .
- [ListTagsForResource](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListTagsForResource.html) â See [Listing tags for a resource](https://docs.aws.amazon.com/healthimaging/latest/devguide/list-tag-resource.html) .
- [UntagResource](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_UntagResource.html) â See [Untagging a resource](https://docs.aws.amazon.com/healthimaging/latest/devguide/untag-resource.html) .

## Available Commands

- [copy-image-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/copy-image-set.html)
- [create-datastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/create-datastore.html)
- [delete-datastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/delete-datastore.html)
- [delete-image-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/delete-image-set.html)
- [get-datastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-datastore.html)
- [get-dicom-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-dicom-import-job.html)
- [get-image-frame](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-frame.html)
- [get-image-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-set.html)
- [get-image-set-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-set-metadata.html)
- [list-datastores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-datastores.html)
- [list-dicom-import-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-dicom-import-jobs.html)
- [list-image-set-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-image-set-versions.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-tags-for-resource.html)
- [search-image-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/search-image-sets.html)
- [start-dicom-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/start-dicom-import-job.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/untag-resource.html)
- [update-image-set-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/update-image-set-metadata.html)