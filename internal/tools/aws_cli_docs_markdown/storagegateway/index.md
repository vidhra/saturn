# storagegatewayÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# storagegateway

## Description

### Warning

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/) .

Storage Gateway is the service that connects an on-premises software appliance with cloud-based storage to provide seamless and secure integration between an organizationâs on-premises IT environment and the Amazon Web Services storage infrastructure. The service enables you to securely upload data to the Amazon Web Services Cloud for cost effective backup and rapid disaster recovery.

Use the following links to get started using the *Storage Gateway Service API Reference* :

- [Storage Gateway required request headers](https://docs.aws.amazon.com/storagegateway/latest/userguide/AWSStorageGatewayAPI.html#AWSStorageGatewayHTTPRequestsHeaders) : Describes the required headers that you must send with every POST request to Storage Gateway.
- [Signing requests](https://docs.aws.amazon.com/storagegateway/latest/userguide/AWSStorageGatewayAPI.html#AWSStorageGatewaySigningRequests) : Storage Gateway requires that you authenticate every request you send; this topic describes how sign such a request.
- [Error responses](https://docs.aws.amazon.com/storagegateway/latest/userguide/AWSStorageGatewayAPI.html#APIErrorResponses) : Provides reference information about Storage Gateway errors.
- [Operations in Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_Operations.html) : Contains detailed descriptions of all Storage Gateway operations, their request parameters, response elements, possible errors, and examples of requests and responses.
- [Storage Gateway endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sg.html) : Provides a list of each Amazon Web Services Region and the endpoints available for use with Storage Gateway.

### Note

Storage Gateway resource IDs are in uppercase. When you use these resource IDs with the Amazon EC2 API, EC2 expects resource IDs in lowercase. You must change your resource ID to lowercase to use it with the EC2 API. For example, in Storage Gateway the ID for a volume might be `vol-AA22BB012345DAF670` . When you use this ID with the EC2 API, you must change it to `vol-aa22bb012345daf670` . Otherwise, the EC2 API might not behave as expected.

### Warning

IDs for Storage Gateway volumes and Amazon EBS snapshots created from gateway volumes are changing to a longer format. Starting in December 2016, all new volumes and snapshots will be created with a 17-character string. Starting in April 2016, you will be able to use these longer IDs so you can test your systems with the new format. For more information, see [Longer EC2 and EBS resource IDs](http://aws.amazon.com/ec2/faqs/#longer-ids) .

For example, a volume Amazon Resource Name (ARN) with the longer volume ID format looks like the following:

`arn:aws:storagegateway:us-west-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABBCCDDEEFFG` .

A snapshot ID with the longer ID format looks like the following: `snap-78e226633445566ee` .

For more information, see [Announcement: Heads-up â Longer Storage Gateway volume and snapshot IDs coming in 2016](http://forums.aws.amazon.com/ann.jspa?annID=3557) .

## Available Commands

- [activate-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/activate-gateway.html)
- [add-cache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/add-cache.html)
- [add-tags-to-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/add-tags-to-resource.html)
- [add-upload-buffer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/add-upload-buffer.html)
- [add-working-storage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/add-working-storage.html)
- [assign-tape-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/assign-tape-pool.html)
- [associate-file-system](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/associate-file-system.html)
- [attach-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/attach-volume.html)
- [cancel-archival](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/cancel-archival.html)
- [cancel-cache-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/cancel-cache-report.html)
- [cancel-retrieval](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/cancel-retrieval.html)
- [create-cached-iscsi-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-cached-iscsi-volume.html)
- [create-nfs-file-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-nfs-file-share.html)
- [create-smb-file-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-smb-file-share.html)
- [create-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-snapshot.html)
- [create-snapshot-from-volume-recovery-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-snapshot-from-volume-recovery-point.html)
- [create-stored-iscsi-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-stored-iscsi-volume.html)
- [create-tape-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tape-pool.html)
- [create-tape-with-barcode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tape-with-barcode.html)
- [create-tapes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tapes.html)
- [delete-automatic-tape-creation-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-automatic-tape-creation-policy.html)
- [delete-bandwidth-rate-limit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-bandwidth-rate-limit.html)
- [delete-cache-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-cache-report.html)
- [delete-chap-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-chap-credentials.html)
- [delete-file-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-file-share.html)
- [delete-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-gateway.html)
- [delete-snapshot-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-snapshot-schedule.html)
- [delete-tape](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape.html)
- [delete-tape-archive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape-archive.html)
- [delete-tape-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape-pool.html)
- [delete-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-volume.html)
- [describe-availability-monitor-test](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-availability-monitor-test.html)
- [describe-bandwidth-rate-limit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-bandwidth-rate-limit.html)
- [describe-bandwidth-rate-limit-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-bandwidth-rate-limit-schedule.html)
- [describe-cache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-cache.html)
- [describe-cache-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-cache-report.html)
- [describe-cached-iscsi-volumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-cached-iscsi-volumes.html)
- [describe-chap-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-chap-credentials.html)
- [describe-file-system-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-file-system-associations.html)
- [describe-gateway-information](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-gateway-information.html)
- [describe-maintenance-start-time](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-maintenance-start-time.html)
- [describe-nfs-file-shares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-nfs-file-shares.html)
- [describe-smb-file-shares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-smb-file-shares.html)
- [describe-smb-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-smb-settings.html)
- [describe-snapshot-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-snapshot-schedule.html)
- [describe-stored-iscsi-volumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-stored-iscsi-volumes.html)
- [describe-tape-archives](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-tape-archives.html)
- [describe-tape-recovery-points](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-tape-recovery-points.html)
- [describe-tapes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-tapes.html)
- [describe-upload-buffer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-upload-buffer.html)
- [describe-vtl-devices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-vtl-devices.html)
- [describe-working-storage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-working-storage.html)
- [detach-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/detach-volume.html)
- [disable-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/disable-gateway.html)
- [disassociate-file-system](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/disassociate-file-system.html)
- [evict-files-failing-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/evict-files-failing-upload.html)
- [join-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/join-domain.html)
- [list-automatic-tape-creation-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-automatic-tape-creation-policies.html)
- [list-cache-reports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-cache-reports.html)
- [list-file-shares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-file-shares.html)
- [list-file-system-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-file-system-associations.html)
- [list-gateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-gateways.html)
- [list-local-disks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-local-disks.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tags-for-resource.html)
- [list-tape-pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tape-pools.html)
- [list-tapes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tapes.html)
- [list-volume-initiators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-volume-initiators.html)
- [list-volume-recovery-points](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-volume-recovery-points.html)
- [list-volumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-volumes.html)
- [notify-when-uploaded](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/notify-when-uploaded.html)
- [refresh-cache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/refresh-cache.html)
- [remove-tags-from-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/remove-tags-from-resource.html)
- [reset-cache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/reset-cache.html)
- [retrieve-tape-archive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/retrieve-tape-archive.html)
- [retrieve-tape-recovery-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/retrieve-tape-recovery-point.html)
- [set-local-console-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/set-local-console-password.html)
- [set-smb-guest-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/set-smb-guest-password.html)
- [shutdown-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/shutdown-gateway.html)
- [start-availability-monitor-test](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/start-availability-monitor-test.html)
- [start-cache-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/start-cache-report.html)
- [start-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/start-gateway.html)
- [update-automatic-tape-creation-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-automatic-tape-creation-policy.html)
- [update-bandwidth-rate-limit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-bandwidth-rate-limit.html)
- [update-bandwidth-rate-limit-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-bandwidth-rate-limit-schedule.html)
- [update-chap-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-chap-credentials.html)
- [update-file-system-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-file-system-association.html)
- [update-gateway-information](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-gateway-information.html)
- [update-gateway-software-now](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-gateway-software-now.html)
- [update-maintenance-start-time](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-maintenance-start-time.html)
- [update-nfs-file-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-nfs-file-share.html)
- [update-smb-file-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-smb-file-share.html)
- [update-smb-file-share-visibility](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-smb-file-share-visibility.html)
- [update-smb-local-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-smb-local-groups.html)
- [update-smb-security-strategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-smb-security-strategy.html)
- [update-snapshot-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-snapshot-schedule.html)
- [update-vtl-device-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-vtl-device-type.html)