# get-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# get-findings

## Description

Describes Amazon GuardDuty findings specified by finding IDs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFindings)

## Synopsis

```
get-findings
--detector-id <value>
--finding-ids <value>
[--sort-criteria <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--detector-id` (string)

The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--finding-ids` (list)

The IDs of the findings that you want to retrieve.

(string)

Syntax:

```
"string" "string" ...
```

`--sort-criteria` (structure)

Represents the criteria used for sorting findings.

AttributeName -> (string)

Represents the finding attribute, such as `accountId` , that sorts the findings.

OrderBy -> (string)

The order by which the sorted findings are to be displayed.

Shorthand Syntax:

```
AttributeName=string,OrderBy=string
```

JSON Syntax:

```
{
  "AttributeName": "string",
  "OrderBy": "ASC"|"DESC"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To retrieve the details of a specific finding**

The following `get-findings` example retrieves the full JSON finding details of the specified finding.

```
aws guardduty get-findings \
    --detector-id 12abc34d567e8fa901bc2d34eexample \
    --finding-id 1ab92989eaf0e742df4a014d5example
```

Output:

```
{
    "Findings": [
        {
            "Resource": {
                "ResourceType": "AccessKey",
                "AccessKeyDetails": {
                    "UserName": "testuser",
                    "UserType": "IAMUser",
                    "PrincipalId": "AIDACKCEVSQ6C2EXAMPLE",
                    "AccessKeyId": "ASIASZ4SI7REEEXAMPLE"
                }
            },
            "Description": "APIs commonly used to discover the users, groups, policies and permissions in an account, was invoked by IAM principal testuser under unusual circumstances. Such activity is not typically seen from this principal.",
            "Service": {
                "Count": 5,
                "Archived": false,
                "ServiceName": "guardduty",
                "EventFirstSeen": "2020-05-26T22:02:24Z",
                "ResourceRole": "TARGET",
                "EventLastSeen": "2020-05-26T22:33:55Z",
                "DetectorId": "d4b040365221be2b54a6264dcexample",
                "Action": {
                    "ActionType": "AWS_API_CALL",
                    "AwsApiCallAction": {
                        "RemoteIpDetails": {
                            "GeoLocation": {
                                "Lat": 51.5164,
                                "Lon": -0.093
                            },
                            "City": {
                                "CityName": "London"
                            },
                            "IpAddressV4": "52.94.36.7",
                            "Organization": {
                                "Org": "Amazon.com",
                                "Isp": "Amazon.com",
                                "Asn": "16509",
                                "AsnOrg": "AMAZON-02"
                            },
                            "Country": {
                                "CountryName": "United Kingdom"
                            }
                        },
                        "Api": "ListPolicyVersions",
                        "ServiceName": "iam.amazonaws.com",
                        "CallerType": "Remote IP"
                    }
                }
            },
            "Title": "Unusual user permission reconnaissance activity by testuser.",
            "Type": "Recon:IAMUser/UserPermissions",
            "Region": "us-east-1",
            "Partition": "aws",
            "Arn": "arn:aws:guardduty:us-east-1:111122223333:detector/d4b040365221be2b54a6264dcexample/finding/1ab92989eaf0e742df4a014d5example",
            "UpdatedAt": "2020-05-26T22:55:21.703Z",
            "SchemaVersion": "2.0",
            "Severity": 5,
            "Id": "1ab92989eaf0e742df4a014d5example",
            "CreatedAt": "2020-05-26T22:21:48.385Z",
            "AccountId": "111122223333"
        }
    ]
}
```

For more information, see [Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html) in the GuardDuty User Guide.

## Output

Findings -> (list)

A list of findings.

(structure)

Contains information about the finding that is generated when abnormal or suspicious activity is detected.

AccountId -> (string)

The ID of the account in which the finding was generated.

Arn -> (string)

The ARN of the finding.

Confidence -> (double)

The confidence score for the finding.

CreatedAt -> (string)

The time and date when the finding was created.

Description -> (string)

The description of the finding.

Id -> (string)

The ID of the finding.

Partition -> (string)

The partition associated with the finding.

Region -> (string)

The Region where the finding was generated.

Resource -> (structure)

Contains information about the Amazon Web Services resource associated with the activity that prompted GuardDuty to generate a finding.

AccessKeyDetails -> (structure)

The IAM access key details (user information) of a user that engaged in the activity that prompted GuardDuty to generate a finding.

AccessKeyId -> (string)

The access key ID of the user.

PrincipalId -> (string)

The principal ID of the user.

UserName -> (string)

The name of the user.

UserType -> (string)

The type of the user.

S3BucketDetails -> (list)

Contains information on the S3 bucket.

(structure)

Contains information on the S3 bucket.

Arn -> (string)

The Amazon Resource Name (ARN) of the S3 bucket.

Name -> (string)

The name of the S3 bucket.

Type -> (string)

Describes whether the bucket is a source or destination bucket.

CreatedAt -> (timestamp)

The date and time the bucket was created at.

Owner -> (structure)

The owner of the S3 bucket.

Id -> (string)

The canonical user ID of the bucket owner. For information about locating your canonical user ID see [Finding Your Account Canonical User ID.](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html#FindingCanonicalId)

Tags -> (list)

All tags attached to the S3 bucket

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

DefaultServerSideEncryption -> (structure)

Describes the server side encryption method used in the S3 bucket.

EncryptionType -> (string)

The type of encryption used for objects within the S3 bucket.

KmsMasterKeyArn -> (string)

The Amazon Resource Name (ARN) of the KMS encryption key. Only available if the bucket `EncryptionType` is `aws:kms` .

PublicAccess -> (structure)

Describes the public access policies that apply to the S3 bucket.

PermissionConfiguration -> (structure)

Contains information about how permissions are configured for the S3 bucket.

BucketLevelPermissions -> (structure)

Contains information about the bucket level permissions for the S3 bucket.

AccessControlList -> (structure)

Contains information on how Access Control Policies are applied to the bucket.

AllowsPublicReadAccess -> (boolean)

A value that indicates whether public read access for the bucket is enabled through an Access Control List (ACL).

AllowsPublicWriteAccess -> (boolean)

A value that indicates whether public write access for the bucket is enabled through an Access Control List (ACL).

BucketPolicy -> (structure)

Contains information on the bucket policies for the S3 bucket.

AllowsPublicReadAccess -> (boolean)

A value that indicates whether public read access for the bucket is enabled through a bucket policy.

AllowsPublicWriteAccess -> (boolean)

A value that indicates whether public write access for the bucket is enabled through a bucket policy.

BlockPublicAccess -> (structure)

Contains information on which account level S3 Block Public Access settings are applied to the S3 bucket.

IgnorePublicAcls -> (boolean)

Indicates if S3 Block Public Access is set to `IgnorePublicAcls` .

RestrictPublicBuckets -> (boolean)

Indicates if S3 Block Public Access is set to `RestrictPublicBuckets` .

BlockPublicAcls -> (boolean)

Indicates if S3 Block Public Access is set to `BlockPublicAcls` .

BlockPublicPolicy -> (boolean)

Indicates if S3 Block Public Access is set to `BlockPublicPolicy` .

AccountLevelPermissions -> (structure)

Contains information about the account level permissions on the S3 bucket.

BlockPublicAccess -> (structure)

Describes the S3 Block Public Access settings of the bucketâs parent account.

IgnorePublicAcls -> (boolean)

Indicates if S3 Block Public Access is set to `IgnorePublicAcls` .

RestrictPublicBuckets -> (boolean)

Indicates if S3 Block Public Access is set to `RestrictPublicBuckets` .

BlockPublicAcls -> (boolean)

Indicates if S3 Block Public Access is set to `BlockPublicAcls` .

BlockPublicPolicy -> (boolean)

Indicates if S3 Block Public Access is set to `BlockPublicPolicy` .

EffectivePermission -> (string)

Describes the effective permission on this bucket after factoring all attached policies.

S3ObjectDetails -> (list)

Information about the S3 object that was scanned.

(structure)

Information about the S3 object that was scanned

ObjectArn -> (string)

Amazon Resource Name (ARN) of the S3 object.

Key -> (string)

Key of the S3 object.

ETag -> (string)

The entity tag is a hash of the S3 object. The ETag reflects changes only to the contents of an object, and not its metadata.

Hash -> (string)

Hash of the threat detected in this finding.

VersionId -> (string)

Version ID of the object.

InstanceDetails -> (structure)

The information about the EC2 instance associated with the activity that prompted GuardDuty to generate a finding.

AvailabilityZone -> (string)

The Availability Zone of the EC2 instance.

IamInstanceProfile -> (structure)

The profile information of the EC2 instance.

Arn -> (string)

The profile ARN of the EC2 instance.

Id -> (string)

The profile ID of the EC2 instance.

ImageDescription -> (string)

The image description of the EC2 instance.

ImageId -> (string)

The image ID of the EC2 instance.

InstanceId -> (string)

The ID of the EC2 instance.

InstanceState -> (string)

The state of the EC2 instance.

InstanceType -> (string)

The type of the EC2 instance.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Outpost. Only applicable to Amazon Web Services Outposts instances.

LaunchTime -> (string)

The launch time of the EC2 instance.

NetworkInterfaces -> (list)

The elastic network interface information of the EC2 instance.

(structure)

Contains information about the elastic network interface of the EC2 instance.

Ipv6Addresses -> (list)

A list of IPv6 addresses for the EC2 instance.

(string)

NetworkInterfaceId -> (string)

The ID of the network interface.

PrivateDnsName -> (string)

The private DNS name of the EC2 instance.

PrivateIpAddress -> (string)

The private IP address of the EC2 instance.

PrivateIpAddresses -> (list)

Other private IP address information of the EC2 instance.

(structure)

Contains other private IP address information of the EC2 instance.

PrivateDnsName -> (string)

The private DNS name of the EC2 instance.

PrivateIpAddress -> (string)

The private IP address of the EC2 instance.

PublicDnsName -> (string)

The public DNS name of the EC2 instance.

PublicIp -> (string)

The public IP address of the EC2 instance.

SecurityGroups -> (list)

The security groups associated with the EC2 instance.

(structure)

Contains information about the security groups associated with the EC2 instance.

GroupId -> (string)

The security group ID of the EC2 instance.

GroupName -> (string)

The security group name of the EC2 instance.

SubnetId -> (string)

The subnet ID of the EC2 instance.

VpcId -> (string)

The VPC ID of the EC2 instance.

Platform -> (string)

The platform of the EC2 instance.

ProductCodes -> (list)

The product code of the EC2 instance.

(structure)

Contains information about the product code for the EC2 instance.

Code -> (string)

The product code information.

ProductType -> (string)

The product code type.

Tags -> (list)

The tags of the EC2 instance.

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

EksClusterDetails -> (structure)

Details about the EKS cluster involved in a Kubernetes finding.

Name -> (string)

EKS cluster name.

Arn -> (string)

EKS cluster ARN.

VpcId -> (string)

The VPC ID to which the EKS cluster is attached.

Status -> (string)

The EKS cluster status.

Tags -> (list)

The EKS cluster tags.

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

CreatedAt -> (timestamp)

The timestamp when the EKS cluster was created.

KubernetesDetails -> (structure)

Details about the Kubernetes user and workload involved in a Kubernetes finding.

KubernetesUserDetails -> (structure)

Details about the Kubernetes user involved in a Kubernetes finding.

Username -> (string)

The username of the user who called the Kubernetes API.

Uid -> (string)

The user ID of the user who called the Kubernetes API.

Groups -> (list)

The groups that include the user who called the Kubernetes API.

(string)

SessionName -> (list)

Entity that assumes the IAM role when Kubernetes RBAC permissions are assigned to that role.

(string)

ImpersonatedUser -> (structure)

Information about the impersonated user.

Username -> (string)

Information about the `username` that was being impersonated.

Groups -> (list)

The `group` to which the user name belongs.

(string)

KubernetesWorkloadDetails -> (structure)

Details about the Kubernetes workload involved in a Kubernetes finding.

Name -> (string)

Kubernetes workload name.

Type -> (string)

Kubernetes workload type (e.g. Pod, Deployment, etc.).

Uid -> (string)

Kubernetes workload ID.

Namespace -> (string)

Kubernetes namespace that the workload is part of.

HostNetwork -> (boolean)

Whether the hostNetwork flag is enabled for the pods included in the workload.

Containers -> (list)

Containers running as part of the Kubernetes workload.

(structure)

Details of a container.

ContainerRuntime -> (string)

The container runtime (such as, Docker or containerd) used to run the container.

Id -> (string)

Container ID.

Name -> (string)

Container name.

Image -> (string)

Container image.

ImagePrefix -> (string)

Part of the image name before the last slash. For example, imagePrefix for public.ecr.aws/amazonlinux/amazonlinux:latest would be public.ecr.aws/amazonlinux. If the image name is relative and does not have a slash, this field is empty.

VolumeMounts -> (list)

Container volume mounts.

(structure)

Container volume mount.

Name -> (string)

Volume mount name.

MountPath -> (string)

Volume mount path.

SecurityContext -> (structure)

Container security context.

Privileged -> (boolean)

Whether the container is privileged.

AllowPrivilegeEscalation -> (boolean)

Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process.

Volumes -> (list)

Volumes used by the Kubernetes workload.

(structure)

Volume used by the Kubernetes workload.

Name -> (string)

Volume name.

HostPath -> (structure)

Represents a pre-existing file or directory on the host machine that the volume maps to.

Path -> (string)

Path of the file or directory on the host that the volume maps to.

ServiceAccountName -> (string)

The service account name that is associated with a Kubernetes workload.

HostIPC -> (boolean)

Whether the host IPC flag is enabled for the pods in the workload.

HostPID -> (boolean)

Whether the host PID flag is enabled for the pods in the workload.

ResourceType -> (string)

The type of Amazon Web Services resource.

EbsVolumeDetails -> (structure)

Contains list of scanned and skipped EBS volumes with details.

ScannedVolumeDetails -> (list)

List of EBS volumes that were scanned.

(structure)

Contains EBS volume details.

VolumeArn -> (string)

EBS volume ARN information.

VolumeType -> (string)

The EBS volume type.

DeviceName -> (string)

The device name for the EBS volume.

VolumeSizeInGB -> (integer)

EBS volume size in GB.

EncryptionType -> (string)

EBS volume encryption type.

SnapshotArn -> (string)

Snapshot ARN of the EBS volume.

KmsKeyArn -> (string)

KMS key ARN used to encrypt the EBS volume.

SkippedVolumeDetails -> (list)

List of EBS volumes that were skipped from the malware scan.

(structure)

Contains EBS volume details.

VolumeArn -> (string)

EBS volume ARN information.

VolumeType -> (string)

The EBS volume type.

DeviceName -> (string)

The device name for the EBS volume.

VolumeSizeInGB -> (integer)

EBS volume size in GB.

EncryptionType -> (string)

EBS volume encryption type.

SnapshotArn -> (string)

Snapshot ARN of the EBS volume.

KmsKeyArn -> (string)

KMS key ARN used to encrypt the EBS volume.

EcsClusterDetails -> (structure)

Contains information about the details of the ECS Cluster.

Name -> (string)

The name of the ECS Cluster.

Arn -> (string)

The Amazon Resource Name (ARN) that identifies the cluster.

Status -> (string)

The status of the ECS cluster.

ActiveServicesCount -> (integer)

The number of services that are running on the cluster in an ACTIVE state.

RegisteredContainerInstancesCount -> (integer)

The number of container instances registered into the cluster.

RunningTasksCount -> (integer)

The number of tasks in the cluster that are in the RUNNING state.

Tags -> (list)

The tags of the ECS Cluster.

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

TaskDetails -> (structure)

Contains information about the details of the ECS Task.

Arn -> (string)

The Amazon Resource Name (ARN) of the task.

DefinitionArn -> (string)

The ARN of the task definition that creates the task.

Version -> (string)

The version counter for the task.

TaskCreatedAt -> (timestamp)

The Unix timestamp for the time when the task was created.

StartedAt -> (timestamp)

The Unix timestamp for the time when the task started.

StartedBy -> (string)

Contains the tag specified when a task is started.

Tags -> (list)

The tags of the ECS Task.

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

Volumes -> (list)

The list of data volume definitions for the task.

(structure)

Volume used by the Kubernetes workload.

Name -> (string)

Volume name.

HostPath -> (structure)

Represents a pre-existing file or directory on the host machine that the volume maps to.

Path -> (string)

Path of the file or directory on the host that the volume maps to.

Containers -> (list)

The containers thatâs associated with the task.

(structure)

Details of a container.

ContainerRuntime -> (string)

The container runtime (such as, Docker or containerd) used to run the container.

Id -> (string)

Container ID.

Name -> (string)

Container name.

Image -> (string)

Container image.

ImagePrefix -> (string)

Part of the image name before the last slash. For example, imagePrefix for public.ecr.aws/amazonlinux/amazonlinux:latest would be public.ecr.aws/amazonlinux. If the image name is relative and does not have a slash, this field is empty.

VolumeMounts -> (list)

Container volume mounts.

(structure)

Container volume mount.

Name -> (string)

Volume mount name.

MountPath -> (string)

Volume mount path.

SecurityContext -> (structure)

Container security context.

Privileged -> (boolean)

Whether the container is privileged.

AllowPrivilegeEscalation -> (boolean)

Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process.

Group -> (string)

The name of the task group thatâs associated with the task.

LaunchType -> (string)

A capacity on which the task is running. For example, `Fargate` and `EC2` .

ContainerDetails -> (structure)

Details of a container.

ContainerRuntime -> (string)

The container runtime (such as, Docker or containerd) used to run the container.

Id -> (string)

Container ID.

Name -> (string)

Container name.

Image -> (string)

Container image.

ImagePrefix -> (string)

Part of the image name before the last slash. For example, imagePrefix for public.ecr.aws/amazonlinux/amazonlinux:latest would be public.ecr.aws/amazonlinux. If the image name is relative and does not have a slash, this field is empty.

VolumeMounts -> (list)

Container volume mounts.

(structure)

Container volume mount.

Name -> (string)

Volume mount name.

MountPath -> (string)

Volume mount path.

SecurityContext -> (structure)

Container security context.

Privileged -> (boolean)

Whether the container is privileged.

AllowPrivilegeEscalation -> (boolean)

Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process.

RdsDbInstanceDetails -> (structure)

Contains information about the database instance to which an anomalous login attempt was made.

DbInstanceIdentifier -> (string)

The identifier associated to the database instance that was involved in the finding.

Engine -> (string)

The database engine of the database instance involved in the finding.

EngineVersion -> (string)

The version of the database engine that was involved in the finding.

DbClusterIdentifier -> (string)

The identifier of the database cluster that contains the database instance ID involved in the finding.

DbInstanceArn -> (string)

The Amazon Resource Name (ARN) that identifies the database instance involved in the finding.

Tags -> (list)

Information about the tag key-value pairs.

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

RdsLimitlessDbDetails -> (structure)

Contains information about the RDS Limitless database that was involved in a GuardDuty finding.

DbShardGroupIdentifier -> (string)

The name associated with the Limitless DB shard group.

DbShardGroupResourceId -> (string)

The resource identifier of the DB shard group within the Limitless Database.

DbShardGroupArn -> (string)

The Amazon Resource Name (ARN) that identifies the DB shard group.

Engine -> (string)

The database engine of the database instance involved in the finding.

EngineVersion -> (string)

The version of the database engine.

DbClusterIdentifier -> (string)

The name of the database cluster that is a part of the Limitless Database.

Tags -> (list)

Information about the tag key-value pair.

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

RdsDbUserDetails -> (structure)

Contains information about the user details through which anomalous login attempt was made.

User -> (string)

The user name used in the anomalous login attempt.

Application -> (string)

The application name used in the anomalous login attempt.

Database -> (string)

The name of the database instance involved in the anomalous login attempt.

Ssl -> (string)

The version of the Secure Socket Layer (SSL) used for the network.

AuthMethod -> (string)

The authentication method used by the user involved in the finding.

LambdaDetails -> (structure)

Contains information about the Lambda function that was involved in a finding.

FunctionArn -> (string)

Amazon Resource Name (ARN) of the Lambda function.

FunctionName -> (string)

Name of the Lambda function.

Description -> (string)

Description of the Lambda function.

LastModifiedAt -> (timestamp)

The timestamp when the Lambda function was last modified. This field is in the UTC date string format `(2023-03-22T19:37:20.168Z)` .

RevisionId -> (string)

The revision ID of the Lambda function version.

FunctionVersion -> (string)

The version of the Lambda function.

Role -> (string)

The execution role of the Lambda function.

VpcConfig -> (structure)

Amazon Virtual Private Cloud configuration details associated with your Lambda function.

SubnetIds -> (list)

The identifiers of the subnets that are associated with your Lambda function.

(string)

VpcId -> (string)

The identifier of the Amazon Virtual Private Cloud.

SecurityGroups -> (list)

The identifier of the security group attached to the Lambda function.

(structure)

Contains information about the security groups associated with the EC2 instance.

GroupId -> (string)

The security group ID of the EC2 instance.

GroupName -> (string)

The security group name of the EC2 instance.

Tags -> (list)

A list of tags attached to this resource, listed in the format of `key` :`value` pair.

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

SchemaVersion -> (string)

The version of the schema used for the finding.

Service -> (structure)

Contains additional information about the generated finding.

Action -> (structure)

Information about the activity that is described in a finding.

ActionType -> (string)

The GuardDuty finding activity type.

AwsApiCallAction -> (structure)

Information about the AWS_API_CALL action described in this finding.

Api -> (string)

The Amazon Web Services API name.

CallerType -> (string)

The Amazon Web Services API caller type.

DomainDetails -> (structure)

The domain information for the Amazon Web Services API call.

Domain -> (string)

The domain information for the Amazon Web Services API call.

ErrorCode -> (string)

The error code of the failed Amazon Web Services API action.

UserAgent -> (string)

The agent through which the API request was made.

RemoteIpDetails -> (structure)

The remote IP information of the connection that initiated the Amazon Web Services API call.

City -> (structure)

The city information of the remote IP address.

CityName -> (string)

The city name of the remote IP address.

Country -> (structure)

The country code of the remote IP address.

CountryCode -> (string)

The country code of the remote IP address.

CountryName -> (string)

The country name of the remote IP address.

GeoLocation -> (structure)

The location information of the remote IP address.

Lat -> (double)

The latitude information of the remote IP address.

Lon -> (double)

The longitude information of the remote IP address.

IpAddressV4 -> (string)

The IPv4 remote address of the connection.

IpAddressV6 -> (string)

The IPv6 remote address of the connection.

Organization -> (structure)

The ISP organization information of the remote IP address.

Asn -> (string)

The Autonomous System Number (ASN) of the internet provider of the remote IP address.

AsnOrg -> (string)

The organization that registered this ASN.

Isp -> (string)

The ISP information for the internet provider.

Org -> (string)

The name of the internet provider.

ServiceName -> (string)

The Amazon Web Services service name whose API was invoked.

RemoteAccountDetails -> (structure)

The details of the Amazon Web Services account that made the API call. This field appears if the call was made from outside your account.

AccountId -> (string)

The Amazon Web Services account ID of the remote API caller.

Affiliated -> (boolean)

Details on whether the Amazon Web Services account of the remote API caller is related to your GuardDuty environment. If this value is `True` the API caller is affiliated to your account in some way. If it is `False` the API caller is from outside your environment.

AffectedResources -> (map)

The details of the Amazon Web Services account that made the API call. This field identifies the resources that were affected by this API call.

key -> (string)

value -> (string)

DnsRequestAction -> (structure)

Information about the DNS_REQUEST action described in this finding.

Domain -> (string)

The domain information for the DNS query.

Protocol -> (string)

The network connection protocol observed in the activity that prompted GuardDuty to generate the finding.

Blocked -> (boolean)

Indicates whether the targeted port is blocked.

DomainWithSuffix -> (string)

The second and top level domain involved in the activity that potentially prompted GuardDuty to generate this finding. For a list of top-level and second-level domains, see [public suffix list](https://publicsuffix.org/) .

NetworkConnectionAction -> (structure)

Information about the NETWORK_CONNECTION action described in this finding.

Blocked -> (boolean)

Indicates whether EC2 blocked the network connection to your instance.

ConnectionDirection -> (string)

The network connection direction.

LocalPortDetails -> (structure)

The local port information of the connection.

Port -> (integer)

The port number of the local connection.

PortName -> (string)

The port name of the local connection.

Protocol -> (string)

The network connection protocol.

LocalIpDetails -> (structure)

The local IP information of the connection.

IpAddressV4 -> (string)

The IPv4 local address of the connection.

IpAddressV6 -> (string)

The IPv6 local address of the connection.

LocalNetworkInterface -> (string)

The EC2 instanceâs local elastic network interface utilized for the connection.

RemoteIpDetails -> (structure)

The remote IP information of the connection.

City -> (structure)

The city information of the remote IP address.

CityName -> (string)

The city name of the remote IP address.

Country -> (structure)

The country code of the remote IP address.

CountryCode -> (string)

The country code of the remote IP address.

CountryName -> (string)

The country name of the remote IP address.

GeoLocation -> (structure)

The location information of the remote IP address.

Lat -> (double)

The latitude information of the remote IP address.

Lon -> (double)

The longitude information of the remote IP address.

IpAddressV4 -> (string)

The IPv4 remote address of the connection.

IpAddressV6 -> (string)

The IPv6 remote address of the connection.

Organization -> (structure)

The ISP organization information of the remote IP address.

Asn -> (string)

The Autonomous System Number (ASN) of the internet provider of the remote IP address.

AsnOrg -> (string)

The organization that registered this ASN.

Isp -> (string)

The ISP information for the internet provider.

Org -> (string)

The name of the internet provider.

RemotePortDetails -> (structure)

The remote port information of the connection.

Port -> (integer)

The port number of the remote connection.

PortName -> (string)

The port name of the remote connection.

PortProbeAction -> (structure)

Information about the PORT_PROBE action described in this finding.

Blocked -> (boolean)

Indicates whether EC2 blocked the port probe to the instance, such as with an ACL.

PortProbeDetails -> (list)

A list of objects related to port probe details.

(structure)

Contains information about the port probe details.

LocalPortDetails -> (structure)

The local port information of the connection.

Port -> (integer)

The port number of the local connection.

PortName -> (string)

The port name of the local connection.

LocalIpDetails -> (structure)

The local IP information of the connection.

IpAddressV4 -> (string)

The IPv4 local address of the connection.

IpAddressV6 -> (string)

The IPv6 local address of the connection.

RemoteIpDetails -> (structure)

The remote IP information of the connection.

City -> (structure)

The city information of the remote IP address.

CityName -> (string)

The city name of the remote IP address.

Country -> (structure)

The country code of the remote IP address.

CountryCode -> (string)

The country code of the remote IP address.

CountryName -> (string)

The country name of the remote IP address.

GeoLocation -> (structure)

The location information of the remote IP address.

Lat -> (double)

The latitude information of the remote IP address.

Lon -> (double)

The longitude information of the remote IP address.

IpAddressV4 -> (string)

The IPv4 remote address of the connection.

IpAddressV6 -> (string)

The IPv6 remote address of the connection.

Organization -> (structure)

The ISP organization information of the remote IP address.

Asn -> (string)

The Autonomous System Number (ASN) of the internet provider of the remote IP address.

AsnOrg -> (string)

The organization that registered this ASN.

Isp -> (string)

The ISP information for the internet provider.

Org -> (string)

The name of the internet provider.

KubernetesApiCallAction -> (structure)

Information about the Kubernetes API call action described in this finding.

RequestUri -> (string)

The Kubernetes API request URI.

Verb -> (string)

The Kubernetes API request HTTP verb.

SourceIps -> (list)

The IP of the Kubernetes API caller and the IPs of any proxies or load balancers between the caller and the API endpoint.

(string)

UserAgent -> (string)

The user agent of the caller of the Kubernetes API.

RemoteIpDetails -> (structure)

Contains information about the remote IP address of the connection.

City -> (structure)

The city information of the remote IP address.

CityName -> (string)

The city name of the remote IP address.

Country -> (structure)

The country code of the remote IP address.

CountryCode -> (string)

The country code of the remote IP address.

CountryName -> (string)

The country name of the remote IP address.

GeoLocation -> (structure)

The location information of the remote IP address.

Lat -> (double)

The latitude information of the remote IP address.

Lon -> (double)

The longitude information of the remote IP address.

IpAddressV4 -> (string)

The IPv4 remote address of the connection.

IpAddressV6 -> (string)

The IPv6 remote address of the connection.

Organization -> (structure)

The ISP organization information of the remote IP address.

Asn -> (string)

The Autonomous System Number (ASN) of the internet provider of the remote IP address.

AsnOrg -> (string)

The organization that registered this ASN.

Isp -> (string)

The ISP information for the internet provider.

Org -> (string)

The name of the internet provider.

StatusCode -> (integer)

The resulting HTTP response code of the Kubernetes API call action.

Parameters -> (string)

Parameters related to the Kubernetes API call action.

Resource -> (string)

The resource component in the Kubernetes API call action.

Subresource -> (string)

The name of the sub-resource in the Kubernetes API call action.

Namespace -> (string)

The name of the namespace where the Kubernetes API call action takes place.

ResourceName -> (string)

The name of the resource in the Kubernetes API call action.

RdsLoginAttemptAction -> (structure)

Information about `RDS_LOGIN_ATTEMPT` action described in this finding.

RemoteIpDetails -> (structure)

Contains information about the remote IP address of the connection.

City -> (structure)

The city information of the remote IP address.

CityName -> (string)

The city name of the remote IP address.

Country -> (structure)

The country code of the remote IP address.

CountryCode -> (string)

The country code of the remote IP address.

CountryName -> (string)

The country name of the remote IP address.

GeoLocation -> (structure)

The location information of the remote IP address.

Lat -> (double)

The latitude information of the remote IP address.

Lon -> (double)

The longitude information of the remote IP address.

IpAddressV4 -> (string)

The IPv4 remote address of the connection.

IpAddressV6 -> (string)

The IPv6 remote address of the connection.

Organization -> (structure)

The ISP organization information of the remote IP address.

Asn -> (string)

The Autonomous System Number (ASN) of the internet provider of the remote IP address.

AsnOrg -> (string)

The organization that registered this ASN.

Isp -> (string)

The ISP information for the internet provider.

Org -> (string)

The name of the internet provider.

LoginAttributes -> (list)

Indicates the login attributes used in the login attempt.

(structure)

Information about the login attempts.

User -> (string)

Indicates the user name which attempted to log in.

Application -> (string)

Indicates the application name used to attempt log in.

FailedLoginAttempts -> (integer)

Represents the sum of failed (unsuccessful) login attempts made to establish a connection to the database instance.

SuccessfulLoginAttempts -> (integer)

Represents the sum of successful connections (a correct combination of login attributes) made to the database instance by the actor.

KubernetesPermissionCheckedDetails -> (structure)

Information whether the user has the permission to use a specific Kubernetes API.

Verb -> (string)

The verb component of the Kubernetes API call. For example, when you check whether or not you have the permission to call the `CreatePod` API, the verb component will be `Create` .

Resource -> (string)

The Kubernetes resource with which your Kubernetes API call will interact.

Namespace -> (string)

The namespace where the Kubernetes API action will take place.

Allowed -> (boolean)

Information whether the user has the permission to call the Kubernetes API.

KubernetesRoleBindingDetails -> (structure)

Information about the role binding that grants the permission defined in a Kubernetes role.

Kind -> (string)

The kind of the role. For role binding, this value will be `RoleBinding` .

Name -> (string)

The name of the `RoleBinding` .

Uid -> (string)

The unique identifier of the role binding.

RoleRefName -> (string)

The name of the role being referenced. This must match the name of the `Role` or `ClusterRole` that you want to bind to.

RoleRefKind -> (string)

The type of the role being referenced. This could be either `Role` or `ClusterRole` .

KubernetesRoleDetails -> (structure)

Information about the Kubernetes role name and role type.

Kind -> (string)

The kind of role. For this API, the value of `kind` will be `Role` .

Name -> (string)

The name of the Kubernetes role.

Uid -> (string)

The unique identifier of the Kubernetes role name.

Evidence -> (structure)

An evidence object associated with the service.

ThreatIntelligenceDetails -> (list)

A list of threat intelligence details related to the evidence.

(structure)

An instance of a threat intelligence detail that constitutes evidence for the finding.

ThreatListName -> (string)

The name of the threat intelligence list that triggered the finding.

ThreatNames -> (list)

A list of names of the threats in the threat intelligence list that triggered the finding.

(string)

ThreatFileSha256 -> (string)

SHA256 of the file that generated the finding.

Archived -> (boolean)

Indicates whether this finding is archived.

Count -> (integer)

The total count of the occurrences of this finding type.

DetectorId -> (string)

The detector ID for the GuardDuty service.

EventFirstSeen -> (string)

The first-seen timestamp of the activity that prompted GuardDuty to generate this finding.

EventLastSeen -> (string)

The last-seen timestamp of the activity that prompted GuardDuty to generate this finding.

ResourceRole -> (string)

The resource role information for this finding.

ServiceName -> (string)

The name of the Amazon Web Services service (GuardDuty) that generated a finding.

UserFeedback -> (string)

Feedback that was submitted about the finding.

AdditionalInfo -> (structure)

Contains additional information about the generated finding.

Value -> (string)

This field specifies the value of the additional information.

Type -> (string)

Describes the type of the additional information.

FeatureName -> (string)

The name of the feature that generated a finding.

EbsVolumeScanDetails -> (structure)

Returns details from the malware scan that created a finding.

ScanId -> (string)

Unique Id of the malware scan that generated the finding.

ScanStartedAt -> (timestamp)

Returns the start date and time of the malware scan.

ScanCompletedAt -> (timestamp)

Returns the completion date and time of the malware scan.

TriggerFindingId -> (string)

GuardDuty finding ID that triggered a malware scan.

Sources -> (list)

Contains list of threat intelligence sources used to detect threats.

(string)

ScanDetections -> (structure)

Contains a complete view providing malware scan result details.

ScannedItemCount -> (structure)

Total number of scanned files.

TotalGb -> (integer)

Total GB of files scanned for malware.

Files -> (integer)

Number of files scanned.

Volumes -> (integer)

Total number of scanned volumes.

ThreatsDetectedItemCount -> (structure)

Total number of infected files.

Files -> (integer)

Total number of infected files.

HighestSeverityThreatDetails -> (structure)

Details of the highest severity threat detected during malware scan and number of infected files.

Severity -> (string)

Severity level of the highest severity threat detected.

ThreatName -> (string)

Threat name of the highest severity threat detected as part of the malware scan.

Count -> (integer)

Total number of infected files with the highest severity threat detected.

ThreatDetectedByName -> (structure)

Contains details about identified threats organized by threat name.

ItemCount -> (integer)

Total number of infected files identified.

UniqueThreatNameCount -> (integer)

Total number of unique threats by name identified, as part of the malware scan.

Shortened -> (boolean)

Flag to determine if the finding contains every single infected file-path and/or every threat.

ThreatNames -> (list)

List of identified threats with details, organized by threat name.

(structure)

Contains files infected with the given threat providing details of malware name and severity.

Name -> (string)

The name of the identified threat.

Severity -> (string)

Severity of threat identified as part of the malware scan.

ItemCount -> (integer)

Total number of files infected with given threat.

FilePaths -> (list)

List of infected files in EBS volume with details.

(structure)

Contains details of infected file including name, file path and hash.

FilePath -> (string)

The file path of the infected file.

VolumeArn -> (string)

EBS volume ARN details of the infected file.

Hash -> (string)

The hash value of the infected file.

FileName -> (string)

File name of the infected file.

ScanType -> (string)

Specifies the scan type that invoked the malware scan.

RuntimeDetails -> (structure)

Information about the process and any required context values for a specific finding

Process -> (structure)

Information about the observed process.

Name -> (string)

The name of the process.

ExecutablePath -> (string)

The absolute path of the process executable file.

ExecutableSha256 -> (string)

The `SHA256` hash of the process executable.

NamespacePid -> (integer)

The ID of the child process.

Pwd -> (string)

The present working directory of the process.

Pid -> (integer)

The ID of the process.

StartTime -> (timestamp)

The time when the process started. This is in UTC format.

Uuid -> (string)

The unique ID assigned to the process by GuardDuty.

ParentUuid -> (string)

The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.

User -> (string)

The user that executed the process.

UserId -> (integer)

The unique ID of the user that executed the process.

Euid -> (integer)

The effective user ID of the user that executed the process.

Lineage -> (list)

Information about the processâs lineage.

(structure)

Information about the runtime process details.

StartTime -> (timestamp)

The time when the process started. This is in UTC format.

NamespacePid -> (integer)

The process ID of the child process.

UserId -> (integer)

The user ID of the user that executed the process.

Name -> (string)

The name of the process.

Pid -> (integer)

The ID of the process.

Uuid -> (string)

The unique ID assigned to the process by GuardDuty.

ExecutablePath -> (string)

The absolute path of the process executable file.

Euid -> (integer)

The effective user ID that was used to execute the process.

ParentUuid -> (string)

The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.

Context -> (structure)

Additional information about the suspicious activity.

ModifyingProcess -> (structure)

Information about the process that modified the current process. This is available for multiple finding types.

Name -> (string)

The name of the process.

ExecutablePath -> (string)

The absolute path of the process executable file.

ExecutableSha256 -> (string)

The `SHA256` hash of the process executable.

NamespacePid -> (integer)

The ID of the child process.

Pwd -> (string)

The present working directory of the process.

Pid -> (integer)

The ID of the process.

StartTime -> (timestamp)

The time when the process started. This is in UTC format.

Uuid -> (string)

The unique ID assigned to the process by GuardDuty.

ParentUuid -> (string)

The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.

User -> (string)

The user that executed the process.

UserId -> (integer)

The unique ID of the user that executed the process.

Euid -> (integer)

The effective user ID of the user that executed the process.

Lineage -> (list)

Information about the processâs lineage.

(structure)

Information about the runtime process details.

StartTime -> (timestamp)

The time when the process started. This is in UTC format.

NamespacePid -> (integer)

The process ID of the child process.

UserId -> (integer)

The user ID of the user that executed the process.

Name -> (string)

The name of the process.

Pid -> (integer)

The ID of the process.

Uuid -> (string)

The unique ID assigned to the process by GuardDuty.

ExecutablePath -> (string)

The absolute path of the process executable file.

Euid -> (integer)

The effective user ID that was used to execute the process.

ParentUuid -> (string)

The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.

ModifiedAt -> (timestamp)

The timestamp at which the process modified the current process. The timestamp is in UTC date string format.

ScriptPath -> (string)

The path to the script that was executed.

LibraryPath -> (string)

The path to the new library that was loaded.

LdPreloadValue -> (string)

The value of the LD_PRELOAD environment variable.

SocketPath -> (string)

The path to the docket socket that was accessed.

RuncBinaryPath -> (string)

The path to the leveraged `runc` implementation.

ReleaseAgentPath -> (string)

The path in the container that modified the release agent file.

MountSource -> (string)

The path on the host that is mounted by the container.

MountTarget -> (string)

The path in the container that is mapped to the host directory.

FileSystemType -> (string)

Represents the type of mounted fileSystem.

Flags -> (list)

Represents options that control the behavior of a runtime operation or action. For example, a filesystem mount operation may contain a read-only flag.

(string)

ModuleName -> (string)

The name of the module loaded into the kernel.

ModuleFilePath -> (string)

The path to the module loaded into the kernel.

ModuleSha256 -> (string)

The `SHA256` hash of the module.

ShellHistoryFilePath -> (string)

The path to the modified shell history file.

TargetProcess -> (structure)

Information about the process that had its memory overwritten by the current process.

Name -> (string)

The name of the process.

ExecutablePath -> (string)

The absolute path of the process executable file.

ExecutableSha256 -> (string)

The `SHA256` hash of the process executable.

NamespacePid -> (integer)

The ID of the child process.

Pwd -> (string)

The present working directory of the process.

Pid -> (integer)

The ID of the process.

StartTime -> (timestamp)

The time when the process started. This is in UTC format.

Uuid -> (string)

The unique ID assigned to the process by GuardDuty.

ParentUuid -> (string)

The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.

User -> (string)

The user that executed the process.

UserId -> (integer)

The unique ID of the user that executed the process.

Euid -> (integer)

The effective user ID of the user that executed the process.

Lineage -> (list)

Information about the processâs lineage.

(structure)

Information about the runtime process details.

StartTime -> (timestamp)

The time when the process started. This is in UTC format.

NamespacePid -> (integer)

The process ID of the child process.

UserId -> (integer)

The user ID of the user that executed the process.

Name -> (string)

The name of the process.

Pid -> (integer)

The ID of the process.

Uuid -> (string)

The unique ID assigned to the process by GuardDuty.

ExecutablePath -> (string)

The absolute path of the process executable file.

Euid -> (integer)

The effective user ID that was used to execute the process.

ParentUuid -> (string)

The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.

AddressFamily -> (string)

Represents the communication protocol associated with the address. For example, the address family `AF_INET` is used for IP version of 4 protocol.

IanaProtocolNumber -> (integer)

Specifies a particular protocol within the address family. Usually there is a single protocol in address families. For example, the address family `AF_INET` only has the IP protocol.

MemoryRegions -> (list)

Specifies the Region of a processâs address space such as stack and heap.

(string)

ToolName -> (string)

Name of the potentially suspicious tool.

ToolCategory -> (string)

Category that the tool belongs to. Some of the examples are Backdoor Tool, Pentest Tool, Network Scanner, and Network Sniffer.

ServiceName -> (string)

Name of the security service that has been potentially disabled.

CommandLineExample -> (string)

Example of the command line involved in the suspicious activity.

ThreatFilePath -> (string)

The suspicious file path for which the threat intelligence details were found.

Detection -> (structure)

Contains information about the detected unusual behavior.

Anomaly -> (structure)

The details about the anomalous activity that caused GuardDuty to generate the finding.

Profiles -> (map)

Information about the types of profiles.

key -> (string)

value -> (map)

key -> (string)

value -> (list)

(structure)

Contains information about the unusual anomalies.

ProfileType -> (string)

The type of behavior of the profile.

ProfileSubtype -> (string)

The frequency of the anomaly.

Observations -> (structure)

The recorded value.

Text -> (list)

The text that was unusual.

(string)

Unusual -> (structure)

Information about the behavior of the anomalies.

Behavior -> (map)

The behavior of the anomalous activity that caused GuardDuty to generate the finding.

key -> (string)

value -> (map)

key -> (string)

value -> (structure)

Contains information about the unusual anomalies.

ProfileType -> (string)

The type of behavior of the profile.

ProfileSubtype -> (string)

The frequency of the anomaly.

Observations -> (structure)

The recorded value.

Text -> (list)

The text that was unusual.

(string)

Sequence -> (structure)

The details about the attack sequence.

Uid -> (string)

Unique identifier of the attack sequence.

Description -> (string)

Description of the attack sequence.

Actors -> (list)

Contains information about the actors involved in the attack sequence.

(structure)

Information about the actors involved in an attack sequence.

Id -> (string)

ID of the threat actor.

User -> (structure)

Contains information about the user credentials used by the threat actor.

Name -> (string)

The name of the user.

Uid -> (string)

The unique identifier of the user.

Type -> (string)

The type of the user.

CredentialUid -> (string)

The credentials of the user ID.

Account -> (structure)

Contains information about the Amazon Web Services account.

Uid -> (string)

ID of the memberâs Amazon Web Services account

Name -> (string)

Name of the memberâs Amazon Web Services account.

Session -> (structure)

Contains information about the user session where the activity initiated.

Uid -> (string)

The unique identifier of the session.

MfaStatus -> (string)

Indicates whether or not multi-factor authencation (MFA) was used during authentication.

In Amazon Web Services CloudTrail, you can find this value as `userIdentity.sessionContext.attributes.mfaAuthenticated` .

CreatedTime -> (timestamp)

The timestamp for when the session was created.

In Amazon Web Services CloudTrail, you can find this value as `userIdentity.sessionContext.attributes.creationDate` .

Issuer -> (string)

Identifier of the session issuer.

In Amazon Web Services CloudTrail, you can find this value as `userIdentity.sessionContext.sessionIssuer.arn` .

Resources -> (list)

Contains information about the resources involved in the attack sequence.

(structure)

Contains information about the Amazon Web Services resource that is associated with the GuardDuty finding.

Uid -> (string)

The unique identifier of the resource.

Name -> (string)

The name of the resource.

AccountId -> (string)

The Amazon Web Services account ID to which the resource belongs.

ResourceType -> (string)

The type of the Amazon Web Services resource.

Region -> (string)

The Amazon Web Services Region where the resource belongs.

Service -> (string)

The Amazon Web Services service of the resource.

CloudPartition -> (string)

The cloud partition within the Amazon Web Services Region to which the resource belongs.

Tags -> (list)

Contains information about the tags associated with the resource.

(structure)

Contains information about a tag key-value pair.

Key -> (string)

Describes the key associated with the tag.

Value -> (string)

Describes the value associated with the tag key.

Data -> (structure)

Contains information about the Amazon Web Services resource associated with the activity that prompted GuardDuty to generate a finding.

S3Bucket -> (structure)

Contains information about the Amazon S3 bucket.

OwnerId -> (string)

The owner ID of the associated S3Amazon S3bucket.

CreatedAt -> (timestamp)

The timestamp at which the Amazon S3 bucket was created.

EncryptionType -> (string)

The type of encryption used for the Amazon S3 buckets and its objects. For more information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) in the *Amazon S3 User Guide* .

EncryptionKeyArn -> (string)

The Amazon Resource Name (ARN) of the encryption key that is used to encrypt the Amazon S3 bucket and its objects.

EffectivePermission -> (string)

Describes the effective permissions on this S3 bucket, after factoring all the attached policies.

PublicReadAccess -> (string)

Indicates whether or not the public read access is allowed for an Amazon S3 bucket.

PublicWriteAccess -> (string)

Indicates whether or not the public write access is allowed for an Amazon S3 bucket.

AccountPublicAccess -> (structure)

Contains information about the public access policies that apply to the Amazon S3 bucket at the account level.

PublicAclAccess -> (string)

Indicates whether or not there is a setting that allows public access to the Amazon S3 buckets through access control lists (ACLs).

PublicPolicyAccess -> (string)

Indicates whether or not there is a setting that allows public access to the Amazon S3 bucket policy.

PublicAclIgnoreBehavior -> (string)

Indicates whether or not there is a setting that ignores all public access control lists (ACLs) on the Amazon S3 bucket and the objects that it contains.

PublicBucketRestrictBehavior -> (string)

Indicates whether or not there is a setting that restricts access to the bucket with specified policies.

BucketPublicAccess -> (structure)

Contains information about public access policies that apply to the Amazon S3 bucket.

PublicAclAccess -> (string)

Indicates whether or not there is a setting that allows public access to the Amazon S3 buckets through access control lists (ACLs).

PublicPolicyAccess -> (string)

Indicates whether or not there is a setting that allows public access to the Amazon S3 bucket policy.

PublicAclIgnoreBehavior -> (string)

Indicates whether or not there is a setting that ignores all public access control lists (ACLs) on the Amazon S3 bucket and the objects that it contains.

PublicBucketRestrictBehavior -> (string)

Indicates whether or not there is a setting that restricts access to the bucket with specified policies.

S3ObjectUids -> (list)

Represents a list of Amazon S3 object identifiers.

(string)

Ec2Instance -> (structure)

Contains information about the Amazon EC2 instance.

AvailabilityZone -> (string)

The availability zone of the Amazon EC2 instance. For more information, see [Availability zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) in the *Amazon EC2 User Guide* .

ImageDescription -> (string)

The image description of the Amazon EC2 instance.

InstanceState -> (string)

The state of the Amazon EC2 instance. For more information, see [Amazon EC2 instance state changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) in the *Amazon EC2 User Guide* .

IamInstanceProfile -> (structure)

Contains information about the EC2 instance profile.

Arn -> (string)

The profile ARN of the EC2 instance.

Id -> (string)

The profile ID of the EC2 instance.

InstanceType -> (string)

Type of the Amazon EC2 instance.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Outpost. This shows applicable Amazon Web Services Outposts instances.

Platform -> (string)

The platform of the Amazon EC2 instance.

ProductCodes -> (list)

The product code of the Amazon EC2 instance.

(structure)

Contains information about the product code for the EC2 instance.

Code -> (string)

The product code information.

ProductType -> (string)

The product code type.

Ec2NetworkInterfaceUids -> (list)

The ID of the network interface.

(string)

AccessKey -> (structure)

Contains information about the IAM access key details of a user that involved in the GuardDuty finding.

PrincipalId -> (string)

Principal ID of the user.

UserName -> (string)

Name of the user.

UserType -> (string)

Type of the user.

Ec2NetworkInterface -> (structure)

Contains information about the elastic network interface of the Amazon EC2 instance.

Ipv6Addresses -> (list)

A list of IPv6 addresses for the Amazon EC2 instance.

(string)

PrivateIpAddresses -> (list)

Other private IP address information of the Amazon EC2 instance.

(structure)

Contains other private IP address information of the EC2 instance.

PrivateDnsName -> (string)

The private DNS name of the EC2 instance.

PrivateIpAddress -> (string)

The private IP address of the EC2 instance.

PublicIp -> (string)

The public IP address of the Amazon EC2 instance.

SecurityGroups -> (list)

The security groups associated with the Amazon EC2 instance.

(structure)

Contains information about the security groups associated with the EC2 instance.

GroupId -> (string)

The security group ID of the EC2 instance.

GroupName -> (string)

The security group name of the EC2 instance.

SubNetId -> (string)

The subnet ID of the Amazon EC2 instance.

VpcId -> (string)

The VPC ID of the Amazon EC2 instance.

S3Object -> (structure)

Contains information about the Amazon S3 object.

ETag -> (string)

The entity tag is a hash of the Amazon S3 object. The ETag reflects changes only to the contents of an object, and not its metadata.

Key -> (string)

The key of the Amazon S3 object.

VersionId -> (string)

The version Id of the Amazon S3 object.

Endpoints -> (list)

Contains information about the network endpoints that were used in the attack sequence.

(structure)

Contains information about network endpoints that were observed in the attack sequence.

Id -> (string)

The ID of the network endpoint.

Ip -> (string)

The IP address associated with the network endpoint.

Domain -> (string)

The domain information for the network endpoint.

Port -> (integer)

The port number associated with the network endpoint.

Location -> (structure)

Information about the location of the network endpoint.

City -> (string)

The name of the city.

Country -> (string)

The name of the country.

Latitude -> (double)

The latitude information of the endpoint location.

Longitude -> (double)

The longitude information of the endpoint location.

AutonomousSystem -> (structure)

The Autonomous System (AS) of the network endpoint.

Name -> (string)

Name associated with the Autonomous System (AS).

Number -> (integer)

The unique number that identifies the Autonomous System (AS).

Connection -> (structure)

Information about the network connection.

Direction -> (string)

The direction in which the network traffic is flowing.

Signals -> (list)

Contains information about the signals involved in the attack sequence.

(structure)

Contains information about the signals involved in the attack sequence.

Uid -> (string)

The unique identifier of the signal.

Type -> (string)

The type of the signal used to identify an attack sequence.

Signals can be GuardDuty findings or activities observed in data sources that GuardDuty monitors. For more information, see [Foundational data sources](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html) in the *Amazon GuardDuty User Guide* .

A signal type can be one of the valid values listed in this API. Here are the related descriptions:

- `FINDING` - Individually generated GuardDuty finding.
- `CLOUD_TRAIL` - Activity observed from CloudTrail logs
- `S3_DATA_EVENTS` - Activity observed from CloudTrail data events for S3. Activities associated with this type will show up only when you have enabled GuardDuty S3 Protection feature in your account. For more information about S3 Protection and steps to enable it, see [S3 Protection](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html) in the *Amazon GuardDuty User Guide* .

Description -> (string)

The description of the signal.

Name -> (string)

The name of the signal. For example, when signal type is `FINDING` , the signal name is the name of the finding.

CreatedAt -> (timestamp)

The timestamp when the first finding or activity related to this signal was observed.

UpdatedAt -> (timestamp)

The timestamp when this signal was last observed.

FirstSeenAt -> (timestamp)

The timestamp when the first finding or activity related to this signal was observed.

LastSeenAt -> (timestamp)

The timestamp when the last finding or activity related to this signal was observed.

Severity -> (double)

The severity associated with the signal. For more information about severity, see [Findings severity levels](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html) in the *Amazon GuardDuty User Guide* .

Count -> (integer)

The number of times this signal was observed.

ResourceUids -> (list)

Information about the unique identifiers of the resources involved in the signal.

(string)

ActorIds -> (list)

Information about the IDs of the threat actors involved in the signal.

(string)

EndpointIds -> (list)

Information about the endpoint IDs associated with this signal.

(string)

SignalIndicators -> (list)

Contains information about the indicators associated with the signals.

(structure)

Contains information about the indicators that include a set of signals observed in an attack sequence.

Key -> (string)

Specific indicator keys observed in the attack sequence. For description of the valid values for key, see [Attack sequence finding details](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-summary.html#guardduty-extended-threat-detection-attack-sequence-finding-details) in the *Amazon GuardDuty User Guide* .

Values -> (list)

Values associated with each indicator key. For example, if the indicator key is `SUSPICIOUS_NETWORK` , then the value will be the name of the network. If the indicator key is `ATTACK_TACTIC` , then the value will be one of the MITRE tactics.

(string)

Title -> (string)

Title describing the indicator.

SequenceIndicators -> (list)

Contains information about the indicators observed in the attack sequence.

(structure)

Contains information about the indicators that include a set of signals observed in an attack sequence.

Key -> (string)

Specific indicator keys observed in the attack sequence. For description of the valid values for key, see [Attack sequence finding details](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-summary.html#guardduty-extended-threat-detection-attack-sequence-finding-details) in the *Amazon GuardDuty User Guide* .

Values -> (list)

Values associated with each indicator key. For example, if the indicator key is `SUSPICIOUS_NETWORK` , then the value will be the name of the network. If the indicator key is `ATTACK_TACTIC` , then the value will be one of the MITRE tactics.

(string)

Title -> (string)

Title describing the indicator.

MalwareScanDetails -> (structure)

Returns details from the malware scan that generated a GuardDuty finding.

Threats -> (list)

Information about the detected threats associated with the generated GuardDuty finding.

(structure)

Information about the detected threats associated with the generated finding.

Name -> (string)

Name of the detected threat that caused GuardDuty to generate this finding.

Source -> (string)

Source of the threat that generated this finding.

ItemPaths -> (list)

Information about the nested item path and hash of the protected resource.

(structure)

Information about the nested item path and hash of the protected resource.

NestedItemPath -> (string)

The nested item path where the infected file was found.

Hash -> (string)

The hash value of the infected resource.

Severity -> (double)

The severity of the finding.

Title -> (string)

The title of the finding.

Type -> (string)

The type of finding.

UpdatedAt -> (string)

The time and date when the finding was last updated.

AssociatedAttackSequenceArn -> (string)

Amazon Resource Name (ARN) associated with the attack sequence finding.