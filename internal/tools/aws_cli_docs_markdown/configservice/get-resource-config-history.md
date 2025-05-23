# get-resource-config-historyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-resource-config-history.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-resource-config-history.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# get-resource-config-history

## Description

### Warning

For accurate reporting on the compliance status, you must record the `AWS::Config::ResourceCompliance` resource type. For more information, see [Selecting Which Resources Config Records](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html) .

Returns a list of `ConfigurationItems` for the specified resource. The list contains details about each state of the resource during the specified time interval. If you specified a retention period to retain your `ConfigurationItems` between a minimum of 30 days and a maximum of 7 years (2557 days), Config returns the `ConfigurationItems` for the specified retention period.

The response is paginated. By default, Config returns a limit of 10 configuration items per page. You can customize this number with the `limit` parameter. The response includes a `nextToken` string. To get the next page of results, run the request again and specify the string for the `nextToken` parameter.

### Note

Each call to the API is limited to span a duration of seven days. It is likely that the number of records returned is smaller than the specified `limit` . In such cases, you can make another call, using the `nextToken` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetResourceConfigHistory)

`get-resource-config-history` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `configurationItems`

## Synopsis

```
get-resource-config-history
--resource-type <value>
--resource-id <value>
[--later-time <value>]
[--earlier-time <value>]
[--chronological-order <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--resource-type` (string)

The resource type.

Possible values:

- `AWS::EC2::CustomerGateway`
- `AWS::EC2::EIP`
- `AWS::EC2::Host`
- `AWS::EC2::Instance`
- `AWS::EC2::InternetGateway`
- `AWS::EC2::NetworkAcl`
- `AWS::EC2::NetworkInterface`
- `AWS::EC2::RouteTable`
- `AWS::EC2::SecurityGroup`
- `AWS::EC2::Subnet`
- `AWS::CloudTrail::Trail`
- `AWS::EC2::Volume`
- `AWS::EC2::VPC`
- `AWS::EC2::VPNConnection`
- `AWS::EC2::VPNGateway`
- `AWS::EC2::RegisteredHAInstance`
- `AWS::EC2::NatGateway`
- `AWS::EC2::EgressOnlyInternetGateway`
- `AWS::EC2::VPCEndpoint`
- `AWS::EC2::VPCEndpointService`
- `AWS::EC2::FlowLog`
- `AWS::EC2::VPCPeeringConnection`
- `AWS::Elasticsearch::Domain`
- `AWS::IAM::Group`
- `AWS::IAM::Policy`
- `AWS::IAM::Role`
- `AWS::IAM::User`
- `AWS::ElasticLoadBalancingV2::LoadBalancer`
- `AWS::ACM::Certificate`
- `AWS::RDS::DBInstance`
- `AWS::RDS::DBSubnetGroup`
- `AWS::RDS::DBSecurityGroup`
- `AWS::RDS::DBSnapshot`
- `AWS::RDS::DBCluster`
- `AWS::RDS::DBClusterSnapshot`
- `AWS::RDS::EventSubscription`
- `AWS::S3::Bucket`
- `AWS::S3::AccountPublicAccessBlock`
- `AWS::Redshift::Cluster`
- `AWS::Redshift::ClusterSnapshot`
- `AWS::Redshift::ClusterParameterGroup`
- `AWS::Redshift::ClusterSecurityGroup`
- `AWS::Redshift::ClusterSubnetGroup`
- `AWS::Redshift::EventSubscription`
- `AWS::SSM::ManagedInstanceInventory`
- `AWS::CloudWatch::Alarm`
- `AWS::CloudFormation::Stack`
- `AWS::ElasticLoadBalancing::LoadBalancer`
- `AWS::AutoScaling::AutoScalingGroup`
- `AWS::AutoScaling::LaunchConfiguration`
- `AWS::AutoScaling::ScalingPolicy`
- `AWS::AutoScaling::ScheduledAction`
- `AWS::DynamoDB::Table`
- `AWS::CodeBuild::Project`
- `AWS::WAF::RateBasedRule`
- `AWS::WAF::Rule`
- `AWS::WAF::RuleGroup`
- `AWS::WAF::WebACL`
- `AWS::WAFRegional::RateBasedRule`
- `AWS::WAFRegional::Rule`
- `AWS::WAFRegional::RuleGroup`
- `AWS::WAFRegional::WebACL`
- `AWS::CloudFront::Distribution`
- `AWS::CloudFront::StreamingDistribution`
- `AWS::Lambda::Function`
- `AWS::NetworkFirewall::Firewall`
- `AWS::NetworkFirewall::FirewallPolicy`
- `AWS::NetworkFirewall::RuleGroup`
- `AWS::ElasticBeanstalk::Application`
- `AWS::ElasticBeanstalk::ApplicationVersion`
- `AWS::ElasticBeanstalk::Environment`
- `AWS::WAFv2::WebACL`
- `AWS::WAFv2::RuleGroup`
- `AWS::WAFv2::IPSet`
- `AWS::WAFv2::RegexPatternSet`
- `AWS::WAFv2::ManagedRuleSet`
- `AWS::XRay::EncryptionConfig`
- `AWS::SSM::AssociationCompliance`
- `AWS::SSM::PatchCompliance`
- `AWS::Shield::Protection`
- `AWS::ShieldRegional::Protection`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ResourceCompliance`
- `AWS::ApiGateway::Stage`
- `AWS::ApiGateway::RestApi`
- `AWS::ApiGatewayV2::Stage`
- `AWS::ApiGatewayV2::Api`
- `AWS::CodePipeline::Pipeline`
- `AWS::ServiceCatalog::CloudFormationProvisionedProduct`
- `AWS::ServiceCatalog::CloudFormationProduct`
- `AWS::ServiceCatalog::Portfolio`
- `AWS::SQS::Queue`
- `AWS::KMS::Key`
- `AWS::QLDB::Ledger`
- `AWS::SecretsManager::Secret`
- `AWS::SNS::Topic`
- `AWS::SSM::FileData`
- `AWS::Backup::BackupPlan`
- `AWS::Backup::BackupSelection`
- `AWS::Backup::BackupVault`
- `AWS::Backup::RecoveryPoint`
- `AWS::ECR::Repository`
- `AWS::ECS::Cluster`
- `AWS::ECS::Service`
- `AWS::ECS::TaskDefinition`
- `AWS::EFS::AccessPoint`
- `AWS::EFS::FileSystem`
- `AWS::EKS::Cluster`
- `AWS::OpenSearch::Domain`
- `AWS::EC2::TransitGateway`
- `AWS::Kinesis::Stream`
- `AWS::Kinesis::StreamConsumer`
- `AWS::CodeDeploy::Application`
- `AWS::CodeDeploy::DeploymentConfig`
- `AWS::CodeDeploy::DeploymentGroup`
- `AWS::EC2::LaunchTemplate`
- `AWS::ECR::PublicRepository`
- `AWS::GuardDuty::Detector`
- `AWS::EMR::SecurityConfiguration`
- `AWS::SageMaker::CodeRepository`
- `AWS::Route53Resolver::ResolverEndpoint`
- `AWS::Route53Resolver::ResolverRule`
- `AWS::Route53Resolver::ResolverRuleAssociation`
- `AWS::DMS::ReplicationSubnetGroup`
- `AWS::DMS::EventSubscription`
- `AWS::MSK::Cluster`
- `AWS::StepFunctions::Activity`
- `AWS::WorkSpaces::Workspace`
- `AWS::WorkSpaces::ConnectionAlias`
- `AWS::SageMaker::Model`
- `AWS::ElasticLoadBalancingV2::Listener`
- `AWS::StepFunctions::StateMachine`
- `AWS::Batch::JobQueue`
- `AWS::Batch::ComputeEnvironment`
- `AWS::AccessAnalyzer::Analyzer`
- `AWS::Athena::WorkGroup`
- `AWS::Athena::DataCatalog`
- `AWS::Detective::Graph`
- `AWS::GlobalAccelerator::Accelerator`
- `AWS::GlobalAccelerator::EndpointGroup`
- `AWS::GlobalAccelerator::Listener`
- `AWS::EC2::TransitGatewayAttachment`
- `AWS::EC2::TransitGatewayRouteTable`
- `AWS::DMS::Certificate`
- `AWS::AppConfig::Application`
- `AWS::AppSync::GraphQLApi`
- `AWS::DataSync::LocationSMB`
- `AWS::DataSync::LocationFSxLustre`
- `AWS::DataSync::LocationS3`
- `AWS::DataSync::LocationEFS`
- `AWS::DataSync::Task`
- `AWS::DataSync::LocationNFS`
- `AWS::EC2::NetworkInsightsAccessScopeAnalysis`
- `AWS::EKS::FargateProfile`
- `AWS::Glue::Job`
- `AWS::GuardDuty::ThreatIntelSet`
- `AWS::GuardDuty::IPSet`
- `AWS::SageMaker::Workteam`
- `AWS::SageMaker::NotebookInstanceLifecycleConfig`
- `AWS::ServiceDiscovery::Service`
- `AWS::ServiceDiscovery::PublicDnsNamespace`
- `AWS::SES::ContactList`
- `AWS::SES::ConfigurationSet`
- `AWS::Route53::HostedZone`
- `AWS::IoTEvents::Input`
- `AWS::IoTEvents::DetectorModel`
- `AWS::IoTEvents::AlarmModel`
- `AWS::ServiceDiscovery::HttpNamespace`
- `AWS::Events::EventBus`
- `AWS::ImageBuilder::ContainerRecipe`
- `AWS::ImageBuilder::DistributionConfiguration`
- `AWS::ImageBuilder::InfrastructureConfiguration`
- `AWS::DataSync::LocationObjectStorage`
- `AWS::DataSync::LocationHDFS`
- `AWS::Glue::Classifier`
- `AWS::Route53RecoveryReadiness::Cell`
- `AWS::Route53RecoveryReadiness::ReadinessCheck`
- `AWS::ECR::RegistryPolicy`
- `AWS::Backup::ReportPlan`
- `AWS::Lightsail::Certificate`
- `AWS::RUM::AppMonitor`
- `AWS::Events::Endpoint`
- `AWS::SES::ReceiptRuleSet`
- `AWS::Events::Archive`
- `AWS::Events::ApiDestination`
- `AWS::Lightsail::Disk`
- `AWS::FIS::ExperimentTemplate`
- `AWS::DataSync::LocationFSxWindows`
- `AWS::SES::ReceiptFilter`
- `AWS::GuardDuty::Filter`
- `AWS::SES::Template`
- `AWS::AmazonMQ::Broker`
- `AWS::AppConfig::Environment`
- `AWS::AppConfig::ConfigurationProfile`
- `AWS::Cloud9::EnvironmentEC2`
- `AWS::EventSchemas::Registry`
- `AWS::EventSchemas::RegistryPolicy`
- `AWS::EventSchemas::Discoverer`
- `AWS::FraudDetector::Label`
- `AWS::FraudDetector::EntityType`
- `AWS::FraudDetector::Variable`
- `AWS::FraudDetector::Outcome`
- `AWS::IoT::Authorizer`
- `AWS::IoT::SecurityProfile`
- `AWS::IoT::RoleAlias`
- `AWS::IoT::Dimension`
- `AWS::IoTAnalytics::Datastore`
- `AWS::Lightsail::Bucket`
- `AWS::Lightsail::StaticIp`
- `AWS::MediaPackage::PackagingGroup`
- `AWS::Route53RecoveryReadiness::RecoveryGroup`
- `AWS::ResilienceHub::ResiliencyPolicy`
- `AWS::Transfer::Workflow`
- `AWS::EKS::IdentityProviderConfig`
- `AWS::EKS::Addon`
- `AWS::Glue::MLTransform`
- `AWS::IoT::Policy`
- `AWS::IoT::MitigationAction`
- `AWS::IoTTwinMaker::Workspace`
- `AWS::IoTTwinMaker::Entity`
- `AWS::IoTAnalytics::Dataset`
- `AWS::IoTAnalytics::Pipeline`
- `AWS::IoTAnalytics::Channel`
- `AWS::IoTSiteWise::Dashboard`
- `AWS::IoTSiteWise::Project`
- `AWS::IoTSiteWise::Portal`
- `AWS::IoTSiteWise::AssetModel`
- `AWS::IVS::Channel`
- `AWS::IVS::RecordingConfiguration`
- `AWS::IVS::PlaybackKeyPair`
- `AWS::KinesisAnalyticsV2::Application`
- `AWS::RDS::GlobalCluster`
- `AWS::S3::MultiRegionAccessPoint`
- `AWS::DeviceFarm::TestGridProject`
- `AWS::Budgets::BudgetsAction`
- `AWS::Lex::Bot`
- `AWS::CodeGuruReviewer::RepositoryAssociation`
- `AWS::IoT::CustomMetric`
- `AWS::Route53Resolver::FirewallDomainList`
- `AWS::RoboMaker::RobotApplicationVersion`
- `AWS::EC2::TrafficMirrorSession`
- `AWS::IoTSiteWise::Gateway`
- `AWS::Lex::BotAlias`
- `AWS::LookoutMetrics::Alert`
- `AWS::IoT::AccountAuditConfiguration`
- `AWS::EC2::TrafficMirrorTarget`
- `AWS::S3::StorageLens`
- `AWS::IoT::ScheduledAudit`
- `AWS::Events::Connection`
- `AWS::EventSchemas::Schema`
- `AWS::MediaPackage::PackagingConfiguration`
- `AWS::KinesisVideo::SignalingChannel`
- `AWS::AppStream::DirectoryConfig`
- `AWS::LookoutVision::Project`
- `AWS::Route53RecoveryControl::Cluster`
- `AWS::Route53RecoveryControl::SafetyRule`
- `AWS::Route53RecoveryControl::ControlPanel`
- `AWS::Route53RecoveryControl::RoutingControl`
- `AWS::Route53RecoveryReadiness::ResourceSet`
- `AWS::RoboMaker::SimulationApplication`
- `AWS::RoboMaker::RobotApplication`
- `AWS::HealthLake::FHIRDatastore`
- `AWS::Pinpoint::Segment`
- `AWS::Pinpoint::ApplicationSettings`
- `AWS::Events::Rule`
- `AWS::EC2::DHCPOptions`
- `AWS::EC2::NetworkInsightsPath`
- `AWS::EC2::TrafficMirrorFilter`
- `AWS::EC2::IPAM`
- `AWS::IoTTwinMaker::Scene`
- `AWS::NetworkManager::TransitGatewayRegistration`
- `AWS::CustomerProfiles::Domain`
- `AWS::AutoScaling::WarmPool`
- `AWS::Connect::PhoneNumber`
- `AWS::AppConfig::DeploymentStrategy`
- `AWS::AppFlow::Flow`
- `AWS::AuditManager::Assessment`
- `AWS::CloudWatch::MetricStream`
- `AWS::DeviceFarm::InstanceProfile`
- `AWS::DeviceFarm::Project`
- `AWS::EC2::EC2Fleet`
- `AWS::EC2::SubnetRouteTableAssociation`
- `AWS::ECR::PullThroughCacheRule`
- `AWS::GroundStation::Config`
- `AWS::ImageBuilder::ImagePipeline`
- `AWS::IoT::FleetMetric`
- `AWS::IoTWireless::ServiceProfile`
- `AWS::NetworkManager::Device`
- `AWS::NetworkManager::GlobalNetwork`
- `AWS::NetworkManager::Link`
- `AWS::NetworkManager::Site`
- `AWS::Panorama::Package`
- `AWS::Pinpoint::App`
- `AWS::Redshift::ScheduledAction`
- `AWS::Route53Resolver::FirewallRuleGroupAssociation`
- `AWS::SageMaker::AppImageConfig`
- `AWS::SageMaker::Image`
- `AWS::ECS::TaskSet`
- `AWS::Cassandra::Keyspace`
- `AWS::Signer::SigningProfile`
- `AWS::Amplify::App`
- `AWS::AppMesh::VirtualNode`
- `AWS::AppMesh::VirtualService`
- `AWS::AppRunner::VpcConnector`
- `AWS::AppStream::Application`
- `AWS::CodeArtifact::Repository`
- `AWS::EC2::PrefixList`
- `AWS::EC2::SpotFleet`
- `AWS::Evidently::Project`
- `AWS::Forecast::Dataset`
- `AWS::IAM::SAMLProvider`
- `AWS::IAM::ServerCertificate`
- `AWS::Pinpoint::Campaign`
- `AWS::Pinpoint::InAppTemplate`
- `AWS::SageMaker::Domain`
- `AWS::Transfer::Agreement`
- `AWS::Transfer::Connector`
- `AWS::KinesisFirehose::DeliveryStream`
- `AWS::Amplify::Branch`
- `AWS::AppIntegrations::EventIntegration`
- `AWS::AppMesh::Route`
- `AWS::Athena::PreparedStatement`
- `AWS::EC2::IPAMScope`
- `AWS::Evidently::Launch`
- `AWS::Forecast::DatasetGroup`
- `AWS::GreengrassV2::ComponentVersion`
- `AWS::GroundStation::MissionProfile`
- `AWS::MediaConnect::FlowEntitlement`
- `AWS::MediaConnect::FlowVpcInterface`
- `AWS::MediaTailor::PlaybackConfiguration`
- `AWS::MSK::Configuration`
- `AWS::Personalize::Dataset`
- `AWS::Personalize::Schema`
- `AWS::Personalize::Solution`
- `AWS::Pinpoint::EmailTemplate`
- `AWS::Pinpoint::EventStream`
- `AWS::ResilienceHub::App`
- `AWS::ACMPCA::CertificateAuthority`
- `AWS::AppConfig::HostedConfigurationVersion`
- `AWS::AppMesh::VirtualGateway`
- `AWS::AppMesh::VirtualRouter`
- `AWS::AppRunner::Service`
- `AWS::CustomerProfiles::ObjectType`
- `AWS::DMS::Endpoint`
- `AWS::EC2::CapacityReservation`
- `AWS::EC2::ClientVpnEndpoint`
- `AWS::Kendra::Index`
- `AWS::KinesisVideo::Stream`
- `AWS::Logs::Destination`
- `AWS::Pinpoint::EmailChannel`
- `AWS::S3::AccessPoint`
- `AWS::NetworkManager::CustomerGatewayAssociation`
- `AWS::NetworkManager::LinkAssociation`
- `AWS::IoTWireless::MulticastGroup`
- `AWS::Personalize::DatasetGroup`
- `AWS::IoTTwinMaker::ComponentType`
- `AWS::CodeBuild::ReportGroup`
- `AWS::SageMaker::FeatureGroup`
- `AWS::MSK::BatchScramSecret`
- `AWS::AppStream::Stack`
- `AWS::IoT::JobTemplate`
- `AWS::IoTWireless::FuotaTask`
- `AWS::IoT::ProvisioningTemplate`
- `AWS::InspectorV2::Filter`
- `AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation`
- `AWS::ServiceDiscovery::Instance`
- `AWS::Transfer::Certificate`
- `AWS::MediaConnect::FlowSource`
- `AWS::APS::RuleGroupsNamespace`
- `AWS::CodeGuruProfiler::ProfilingGroup`
- `AWS::Route53Resolver::ResolverQueryLoggingConfig`
- `AWS::Batch::SchedulingPolicy`
- `AWS::ACMPCA::CertificateAuthorityActivation`
- `AWS::AppMesh::GatewayRoute`
- `AWS::AppMesh::Mesh`
- `AWS::Connect::Instance`
- `AWS::Connect::QuickConnect`
- `AWS::EC2::CarrierGateway`
- `AWS::EC2::IPAMPool`
- `AWS::EC2::TransitGatewayConnect`
- `AWS::EC2::TransitGatewayMulticastDomain`
- `AWS::ECS::CapacityProvider`
- `AWS::IAM::InstanceProfile`
- `AWS::IoT::CACertificate`
- `AWS::IoTTwinMaker::SyncJob`
- `AWS::KafkaConnect::Connector`
- `AWS::Lambda::CodeSigningConfig`
- `AWS::NetworkManager::ConnectPeer`
- `AWS::ResourceExplorer2::Index`
- `AWS::AppStream::Fleet`
- `AWS::Cognito::UserPool`
- `AWS::Cognito::UserPoolClient`
- `AWS::Cognito::UserPoolGroup`
- `AWS::EC2::NetworkInsightsAccessScope`
- `AWS::EC2::NetworkInsightsAnalysis`
- `AWS::Grafana::Workspace`
- `AWS::GroundStation::DataflowEndpointGroup`
- `AWS::ImageBuilder::ImageRecipe`
- `AWS::KMS::Alias`
- `AWS::M2::Environment`
- `AWS::QuickSight::DataSource`
- `AWS::QuickSight::Template`
- `AWS::QuickSight::Theme`
- `AWS::RDS::OptionGroup`
- `AWS::Redshift::EndpointAccess`
- `AWS::Route53Resolver::FirewallRuleGroup`
- `AWS::SSM::Document`

`--resource-id` (string)

The ID of the resource (for example., `sg-xxxxxx` ).

`--later-time` (timestamp)

The chronologically latest time in the time range for which the history requested. If not specified, current time is taken.

`--earlier-time` (timestamp)

The chronologically earliest time in the time range for which the history requested. If not specified, the action returns paginated results that contain configuration items that start when the first configuration item was recorded.

`--chronological-order` (string)

The chronological order for configuration items listed. By default, the results are listed in reverse chronological order.

Possible values:

- `Reverse`
- `Forward`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To get the configuration history of an AWS resource**

The following command returns a list of configuration items for an EC2 instance with an ID of `i-1a2b3c4d`:

```
aws configservice get-resource-config-history --resource-type AWS::EC2::Instance --resource-id i-1a2b3c4d
```

## Output

configurationItems -> (list)

A list that contains the configuration history of one or more resources.

(structure)

A list that contains detailed configurations of a specified resource.

version -> (string)

The version number of the resource configuration.

accountId -> (string)

The 12-digit Amazon Web Services account ID associated with the resource.

configurationItemCaptureTime -> (timestamp)

The time when the recording of configuration changes was initiated for the resource.

configurationItemStatus -> (string)

The configuration item status. Valid values include:

- OK â The resource configuration has been updated
- ResourceDiscovered â The resource was newly discovered
- ResourceNotRecorded â The resource was discovered but its configuration was not recorded since the recorder doesnât record resources of this type
- ResourceDeleted â The resource was deleted
- ResourceDeletedNotRecorded â The resource was deleted but its configuration was not recorded since the recorder doesnât record resources of this type

configurationStateId -> (string)

An identifier that indicates the ordering of the configuration items of a resource.

configurationItemMD5Hash -> (string)

Unique MD5 hash that represents the configuration itemâs state.

You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.

arn -> (string)

Amazon Resource Name (ARN) associated with the resource.

resourceType -> (string)

The type of Amazon Web Services resource.

resourceId -> (string)

The ID of the resource (for example, `sg-xxxxxx` ).

resourceName -> (string)

The custom name of the resource, if available.

awsRegion -> (string)

The region where the resource resides.

availabilityZone -> (string)

The Availability Zone associated with the resource.

resourceCreationTime -> (timestamp)

The time stamp when the resource was created.

tags -> (map)

A mapping of key value tags associated with the resource.

key -> (string)

value -> (string)

relatedEvents -> (list)

A list of CloudTrail event IDs.

A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see [What Is CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html) .

An empty field indicates that the current configuration was not initiated by any event. As of Version 1.3, the relatedEvents field is empty. You can access the [LookupEvents API](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html) in the *CloudTrail API Reference* to retrieve the events for the resource.

(string)

relationships -> (list)

A list of related Amazon Web Services resources.

(structure)

The relationship of the related resource to the main resource.

resourceType -> (string)

The resource type of the related resource.

resourceId -> (string)

The ID of the related resource (for example, `sg-xxxxxx` ).

resourceName -> (string)

The custom name of the related resource, if available.

relationshipName -> (string)

The type of relationship with the related resource.

configuration -> (string)

The description of the resource configuration.

supplementaryConfiguration -> (map)

Configuration attributes that Config returns for certain resource types to supplement the information returned for the `configuration` parameter.

key -> (string)

value -> (string)

recordingFrequency -> (string)

The recording frequency that Config uses to record configuration changes for the resource.

configurationItemDeliveryTime -> (timestamp)

The time when configuration changes for the resource were delivered.

### Note

This field is optional and is not guaranteed to be present in a configuration item (CI). If you are using daily recording, this field will be populated. However, if you are using continuous recording, this field will be omitted since the delivery time is instantaneous as the CI is available right away. For more information on daily recording and continuous recording, see [Recording Frequency](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-recording-frequency) in the *Config Developer Guide* .

nextToken -> (string)

The string that you use in a subsequent request to get the next page of results in a paginated response.