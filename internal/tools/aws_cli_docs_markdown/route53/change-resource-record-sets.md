# change-resource-record-setsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/change-resource-record-sets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/change-resource-record-sets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# change-resource-record-sets

## Description

Creates, changes, or deletes a resource record set, which contains authoritative DNS information for a specified domain name or subdomain name. For example, you can use `ChangeResourceRecordSets` to create a resource record set that routes traffic for test.example.com to a web server that has an IP address of 192.0.2.44.

**Deleting Resource Record Sets**

To delete a resource record set, you must specify all the same values that you specified when you created it.

**Change Batches and Transactional Changes**

The request body must include a document with a `ChangeResourceRecordSetsRequest` element. The request body contains a list of change items, known as a change batch. Change batches are considered transactional changes. Route 53 validates the changes in the request and then either makes all or none of the changes in the change batch request. This ensures that DNS routing isnât adversely affected by partial changes to the resource record sets in a hosted zone.

For example, suppose a change batch request contains two changes: it deletes the `CNAME` resource record set for www.example.com and creates an alias resource record set for www.example.com. If validation for both records succeeds, Route 53 deletes the first resource record set and creates the second resource record set in a single operation. If validation for either the `DELETE` or the `CREATE` action fails, then the request is canceled, and the original `CNAME` record continues to exist.

### Note

If you try to delete the same resource record set more than once in a single change batch, Route 53 returns an `InvalidChangeBatch` error.

**Traffic Flow**

To create resource record sets for complex routing configurations, use either the traffic flow visual editor in the Route 53 console or the API actions for traffic policies and traffic policy instances. Save the configuration as a traffic policy, then associate the traffic policy with one or more domain names (such as example.com) or subdomain names (such as www.example.com), in the same hosted zone or in multiple hosted zones. You can roll back the updates if the new configuration isnât performing as expected. For more information, see [Using Traffic Flow to Route DNS Traffic](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html) in the *Amazon Route 53 Developer Guide* .

**Create, Delete, and Upsert**

Use `ChangeResourceRecordsSetsRequest` to perform the following actions:

- `CREATE` : Creates a resource record set that has the specified values.
- `DELETE` : Deletes an existing resource record set that has the specified values.
- `UPSERT` : If a resource set doesnât exist, Route 53 creates it. If a resource set exists Route 53 updates it with the values in the request.

**Syntaxes for Creating, Updating, and Deleting Resource Record Sets**

The syntax for a request depends on the type of resource record set that you want to create, delete, or update, such as weighted, alias, or failover. The XML elements in your request must appear in the order listed in the syntax.

For an example for each type of resource record set, see âExamples.â

Donât refer to the syntax in the âParameter Syntaxâ section, which includes all of the elements for every kind of resource record set that you can create, delete, or update by using `ChangeResourceRecordSets` .

**Change Propagation to Route 53 DNS Servers**

When you submit a `ChangeResourceRecordSets` request, Route 53 propagates your changes to all of the Route 53 authoritative DNS servers managing the hosted zone. While your changes are propagating, `GetChange` returns a status of `PENDING` . When propagation is complete, `GetChange` returns a status of `INSYNC` . Changes generally propagate to all Route 53 name servers managing the hosted zone within 60 seconds. For more information, see [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) .

**Limits on ChangeResourceRecordSets Requests**

For information about the limits on a `ChangeResourceRecordSets` request, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ChangeResourceRecordSets)

## Synopsis

```
change-resource-record-sets
--hosted-zone-id <value>
--change-batch <value>
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

`--hosted-zone-id` (string)

The ID of the hosted zone that contains the resource record sets that you want to change.

`--change-batch` (structure)

A complex type that contains an optional comment and the `Changes` element.

Comment -> (string)

*Optional:* Any comments you want to include about a change batch request.

Changes -> (list)

Information about the changes to make to the record sets.

(structure)

The information for each resource record set that you want to change.

Action -> (string)

The action to perform:

- `CREATE` : Creates a resource record set that has the specified values.
- `DELETE` : Deletes a existing resource record set.

### Warning

To delete the resource record set that is associated with a traffic policy instance, use [DeleteTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicyInstance.html) . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using `ChangeResourceRecordSets` , Route 53 doesnât automatically delete the traffic policy instance, and youâll continue to be charged for it even though itâs no longer in use.

- `UPSERT` : If a resource record set doesnât already exist, Route 53 creates it. If a resource record set does exist, Route 53 updates it with the values in the request.

ResourceRecordSet -> (structure)

Information about the resource record set to create, delete, or update.

Name -> (string)

For `ChangeResourceRecordSets` requests, the name of the record that you want to create, update, or delete. For `ListResourceRecordSets` responses, the name of a record in the specified hosted zone.

**ChangeResourceRecordSets Only**

Enter a fully qualified domain name, for example, `www.example.com` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats `www.example.com` (without a trailing dot) and `www.example.com.` (with a trailing dot) as identical.

For information about how to specify characters other than `a-z` , `0-9` , and `-` (hyphen) and how to specify internationalized domain names, see [DNS Domain Name Format](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html) in the *Amazon Route 53 Developer Guide* .

You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, `*.example.com` . Note the following:

- The * must replace the entire label. For example, you canât specify `*prod.example.com` or `prod*.example.com` .
- The * canât replace any of the middle labels, for example, marketing.*.example.com.
- If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.

### Warning

You canât use the * wildcard for resource records sets that have a type of NS.

Type -> (string)

The DNS record type. For information about different record types and how data is encoded for them, see [Supported DNS Resource Record Types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html) in the *Amazon Route 53 Developer Guide* .

Valid values for basic resource record sets: `A` | `AAAA` | `CAA` | `CNAME` | `DS` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/change-resource-record-sets.html#id1)`MX` | `NAPTR` | `NS` | `PTR` | `SOA` | `SPF` | `SRV` | `TXT` | `TLSA` | `SSHFP` | `SVCB` | `HTTPS`

Values for weighted, latency, geolocation, and failover resource record sets: `A` | `AAAA` | `CAA` | `CNAME` | `MX` | `NAPTR` | `PTR` | `SPF` | `SRV` | `TXT` | `TLSA` | `SSHFP` | `SVCB` | `HTTPS` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.

Valid values for multivalue answer resource record sets: `A` | `AAAA` | `MX` | `NAPTR` | `PTR` | `SPF` | `SRV` | `TXT` | `CAA` | `TLSA` | `SSHFP` | `SVCB` | `HTTPS`

### Note

SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of `Type` is `SPF` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, ââ¦[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it.â In RFC 7208, see section 14.1, [The SPF DNS Record Type](http://tools.ietf.org/html/rfc7208#section-14.1) .

Values for alias resource record sets:

- **Amazon API Gateway custom regional APIs and edge-optimized APIs:** `A`
- **CloudFront distributions:** `A`   If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of `A` and one with a value of `AAAA` .
- **Amazon API Gateway environment that has a regionalized subdomain** : `A`
- **ELB load balancers:** `A` | `AAAA`
- **Amazon S3 buckets:** `A`
- **Amazon Virtual Private Cloud interface VPC endpoints** `A`
- **Another resource record set in this hosted zone:** Specify the type of the resource record set that youâre creating the alias for. All values are supported except `NS` and `SOA` .

### Note

If youâre creating an alias record that has the same name as the hosted zone (known as the zone apex), you canât route traffic to a record for which the value of `Type` is `CNAME` . This is because the alias record must have the same type as the record youâre routing traffic to, and creating a CNAME record for the zone apex isnât supported even for an alias record.

SetIdentifier -> (string)

*Resource record sets that have a routing policy other than simple:* An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of `SetIdentifier` must be unique for each resource record set.

For information about routing policies, see [Choosing a Routing Policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) in the *Amazon Route 53 Developer Guide* .

Weight -> (long)

*Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resourceâs weight to the total. Note the following:

- You must specify a value for the `Weight` element for every weighted resource record set.
- You can only specify one `ResourceRecord` per weighted resource record set.
- You canât create latency, failover, or geolocation resource record sets that have the same values for the `Name` and `Type` elements as weighted resource record sets.
- You can create a maximum of 100 weighted resource record sets that have the same values for the `Name` and `Type` elements.
- For weighted (but not weighted alias) resource record sets, if you set `Weight` to `0` for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set `Weight` to `0` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting `Weight` to `0` is different when you associate health checks with weighted resource record sets. For more information, see [Options for Configuring Route 53 Active-Active and Active-Passive Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html) in the *Amazon Route 53 Developer Guide* .

Region -> (string)

*Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an Amazon Web Services resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.

When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set.

Note the following:

- You can only specify one `ResourceRecord` per latency resource record set.
- You can only create one latency resource record set for each Amazon EC2 Region.
- You arenât required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for.
- You canât create non-latency resource record sets that have the same values for the `Name` and `Type` elements as latency resource record sets.

GeoLocation -> (structure)

*Geolocation resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of `192.0.2.111` , create a resource record set with a `Type` of `A` and a `ContinentCode` of `AF` .

If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.

You canât create two geolocation resource record sets that specify the same geographic location.

The value `*` in the `CountryCode` element matches all geographic locations that arenât specified in other geolocation resource record sets that have the same values for the `Name` and `Type` elements.

### Warning

Geolocation works by mapping IP addresses to locations. However, some IP addresses arenât mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it canât identify. We recommend that you create a resource record set for which the value of `CountryCode` is `*` . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you havenât created geolocation resource record sets and queries from IP addresses that arenât mapped to a location. If you donât create a `*` resource record set, Route 53 returns a âno answerâ response for queries from those locations.

You canât create non-geolocation resource record sets that have the same values for the `Name` and `Type` elements as geolocation resource record sets.

ContinentCode -> (string)

The two-letter code for the continent.

Amazon Route 53 supports the following continent codes:

- **AF** : Africa
- **AN** : Antarctica
- **AS** : Asia
- **EU** : Europe
- **OC** : Oceania
- **NA** : North America
- **SA** : South America

Constraint: Specifying `ContinentCode` with either `CountryCode` or `SubdivisionCode` returns an `InvalidInput` error.

CountryCode -> (string)

For geolocation resource record sets, the two-letter code for a country.

Amazon Route 53 uses the two-letter country codes that are specified in [ISO standard 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) .

Route 53 also supports the country code **UA** for Ukraine.

SubdivisionCode -> (string)

For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesnât support any other values for `SubdivisionCode` . For a list of state abbreviations, see [Appendix B: TwoâLetter State and Possession Abbreviations](https://pe.usps.com/text/pub28/28apb.htm) on the United States Postal Service website.

If you specify `subdivisioncode` , you must also specify `US` for `CountryCode` .

Failover -> (string)

*Failover resource record sets only:* To configure failover, you add the `Failover` element to two resource record sets. For one resource record set, you specify `PRIMARY` as the value for `Failover` ; for the other resource record set, you specify `SECONDARY` . In addition, you include the `HealthCheckId` element and specify the health check that you want Amazon Route 53 to perform for each resource record set.

Except where noted, the following failover behaviors assume that you have included the `HealthCheckId` element in both resource record sets:

- When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
- When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
- When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
- If you omit the `HealthCheckId` element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.

You canât create non-failover resource record sets that have the same values for the `Name` and `Type` elements as failover resource record sets.

For failover alias resource record sets, you must also include the `EvaluateTargetHealth` element and set the value to true.

For more information about configuring failover for Route 53, see the following topics in the *Amazon Route 53 Developer Guide* :

- [Route 53 Health Checks and DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
- [Configuring Failover in a Private Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html)

MultiValueAnswer -> (boolean)

*Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify `true` for `MultiValueAnswer` . Note the following:

- If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy.
- If you donât associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy.
- Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records.
- If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records.
- When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records.
- If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response.

You canât create multivalue answer alias records.

TTL -> (long)

The resource record cache time to live (TTL), in seconds. Note the following:

- If youâre creating or updating an alias resource record set, omit `TTL` . Amazon Route 53 uses the value of `TTL` for the alias target.
- If youâre associating this resource record set with a health check (if youâre adding a `HealthCheckId` element), we recommend that you specify a `TTL` of 60 seconds or less so clients respond quickly to changes in health status.
- All of the resource record sets in a group of weighted resource record sets must have the same value for `TTL` .
- If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a `TTL` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for `Weight` .

ResourceRecords -> (list)

Information about the resource records to act upon.

### Note

If youâre creating an alias resource record set, omit `ResourceRecords` .

(structure)

Information specific to the resource record.

### Note

If youâre creating an alias resource record set, omit `ResourceRecord` .

Value -> (string)

The current or new DNS record value, not to exceed 4,000 characters. In the case of a `DELETE` action, if the current value does not match the actual value, an error is returned. For descriptions about how to format `Value` for different record types, see [Supported DNS Resource Record Types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html) in the *Amazon Route 53 Developer Guide* .

You can specify more than one value for all record types except `CNAME` and `SOA` .

### Note

If youâre creating an alias resource record set, omit `Value` .

AliasTarget -> (structure)

*Alias resource record sets only:* Information about the Amazon Web Services resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.

If youâre creating resource records sets for a private hosted zone, note the following:

- You canât create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution.
- For information about creating failover resource record sets in a private hosted zone, see [Configuring Failover in a Private Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html) in the *Amazon Route 53 Developer Guide* .

HostedZoneId -> (string)

*Alias resource records sets only* : The value used depends on where you want to route traffic:

Amazon API Gateway custom regional APIs and edge-optimized APIs

Specify the hosted zone ID for your API. You can get the applicable value using the CLI command [get-domain-names](https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html) :

- For regional APIs, specify the value of `regionalHostedZoneId` .
- For edge-optimized APIs, specify the value of `distributionHostedZoneId` .

Amazon Virtual Private Cloud interface VPC endpoint

Specify the hosted zone ID for your interface endpoint. You can get the value of `HostedZoneId` using the CLI command [describe-vpc-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html) .

CloudFront distribution

Specify `Z2FDTNDATAQYW2` .

### Note

Alias resource record sets for CloudFront canât be created in a private zone.

Elastic Beanstalk environment

Specify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see [Elastic Beanstalk endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/elasticbeanstalk.html) in the *Amazon Web Services General Reference* .

ELB load balancer

Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:

- [Elastic Load Balancing endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/elb.html) topic in the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers.
- **Amazon Web Services Management Console** : Go to the Amazon EC2 page, choose **Load Balancers** in the navigation pane, select the load balancer, and get the value of the **Hosted zone** field on the **Description** tab.
- **Elastic Load Balancing API** : Use `DescribeLoadBalancers` to get the applicable value. For more information, see the applicable guide:

- Classic Load Balancers: Use [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html) to get the value of `CanonicalHostedZoneNameId` .
- Application and Network Load Balancers: Use [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) to get the value of `CanonicalHostedZoneId` .
- **CLI** : Use `describe-load-balancers` to get the applicable value. For more information, see the applicable guide:

- Classic Load Balancers: Use [describe-load-balancers](http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html) to get the value of `CanonicalHostedZoneNameId` .
- Application and Network Load Balancers: Use [describe-load-balancers](http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html) to get the value of `CanonicalHostedZoneId` .

Global Accelerator accelerator

Specify `Z2BJ6XQ5FK7U4H` .

An Amazon S3 bucket configured as a static website

Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the table [Amazon S3 Website Endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints) in the *Amazon Web Services General Reference* .

Another Route 53 resource record set in your hosted zone

Specify the hosted zone ID of your hosted zone. (An alias resource record set canât reference a resource record set in a different hosted zone.)

DNSName -> (string)

*Alias resource record sets only:* The value that you specify depends on where you want to route queries:

Amazon API Gateway custom regional APIs and edge-optimized APIs

Specify the applicable domain name for your API. You can get the applicable value using the CLI command [get-domain-names](https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html) :

- For regional APIs, specify the value of `regionalDomainName` .
- For edge-optimized APIs, specify the value of `distributionDomainName` . This is the name of the associated CloudFront distribution, such as `da1b2c3d4e5.cloudfront.net` .

### Note

The name of the record that youâre creating must match a custom domain name for your API, such as `api.example.com` .

Amazon Virtual Private Cloud interface VPC endpoint

Enter the API endpoint for the interface endpoint, such as `vpce-123456789abcdef01-example-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com` . For edge-optimized APIs, this is the domain name for the corresponding CloudFront distribution. You can get the value of `DnsName` using the CLI command [describe-vpc-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html) .

CloudFront distribution

Specify the domain name that CloudFront assigned when you created your distribution.

Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see [Using Alternate Domain Names (CNAMEs)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html) in the *Amazon CloudFront Developer Guide* .

You canât create a resource record set in a private hosted zone to route traffic to a CloudFront distribution.

### Note

For failover alias records, you canât specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you canât include the same alternate domain name in more than one distribution.

Elastic Beanstalk environment

If the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name `my-environment.*us-west-2* .elasticbeanstalk.com` is a regionalized domain name.

### Warning

For environments that were created before early 2016, the domain name doesnât include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you canât create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you canât create a record that routes traffic for example.com to your Elastic Beanstalk environment.

For Elastic Beanstalk environments that have regionalized subdomains, specify the `CNAME` attribute for the environment. You can use the following methods to get the value of the CNAME attribute:

- *Amazon Web Services Management Console* : For information about how to get the value by using the console, see [Using Custom Domains with Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html) in the *Elastic Beanstalk Developer Guide* .
- *Elastic Beanstalk API* : Use the `DescribeEnvironments` action to get the value of the `CNAME` attribute. For more information, see [DescribeEnvironments](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html) in the *Elastic Beanstalk API Reference* .
- *CLI* : Use the `describe-environments` command to get the value of the `CNAME` attribute. For more information, see [describe-environments](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html) in the *CLI Command Reference* .

ELB load balancer

Specify the DNS name that is associated with the load balancer. Get the DNS name by using the Amazon Web Services Management Console, the ELB API, or the CLI.

- **Amazon Web Services Management Console** : Go to the EC2 page, choose **Load Balancers** in the navigation pane, choose the load balancer, choose the **Description** tab, and get the value of the **DNS name** field.  If youâre routing traffic to a Classic Load Balancer, get the value that begins with **dualstack** . If youâre routing traffic to another type of load balancer, get the value that applies to the record type, A or AAAA.
- **Elastic Load Balancing API** : Use `DescribeLoadBalancers` to get the value of `DNSName` . For more information, see the applicable guide:

- Classic Load Balancers: [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html)
- Application and Network Load Balancers: [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html)
- **CLI** : Use `describe-load-balancers` to get the value of `DNSName` . For more information, see the applicable guide:

- Classic Load Balancers: [describe-load-balancers](http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html)
- Application and Network Load Balancers: [describe-load-balancers](http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html)

Global Accelerator accelerator

Specify the DNS name for your accelerator:

- **Global Accelerator API:** To get the DNS name, use [DescribeAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAccelerator.html) .
- **CLI:** To get the DNS name, use [describe-accelerator](https://docs.aws.amazon.com/cli/latest/reference/globalaccelerator/describe-accelerator.html) .

Amazon S3 bucket that is configured as a static website

Specify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, `s3-website.us-east-2.amazonaws.com` . For more information about valid values, see the table [Amazon S3 Website Endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints) in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see [Getting Started with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html) in the *Amazon Route 53 Developer Guide.*

Another Route 53 resource record set

Specify the value of the `Name` element for a resource record set in the current hosted zone.

### Note

If youâre creating an alias record that has the same name as the hosted zone (known as the zone apex), you canât specify the domain name for a record for which the value of `Type` is `CNAME` . This is because the alias record must have the same type as the record that youâre routing traffic to, and creating a CNAME record for the zone apex isnât supported even for an alias record.

EvaluateTargetHealth -> (boolean)

*Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets:* When `EvaluateTargetHealth` is `true` , an alias resource record set inherits the health of the referenced Amazon Web Services resource, such as an ELB load balancer or another resource record set in the hosted zone.

Note the following:

CloudFront distributions

You canât set `EvaluateTargetHealth` to `true` when the alias target is a CloudFront distribution.

Elastic Beanstalk environments that have regionalized subdomains

If you specify an Elastic Beanstalk environment in `DNSName` and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set `EvaluateTargetHealth` to `true` and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any.

If the environment contains a single Amazon EC2 instance, there are no special requirements.

ELB load balancers

Health checking behavior depends on the type of load balancer:

- **Classic Load Balancers** : If you specify an ELB Classic Load Balancer in `DNSName` , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set `EvaluateTargetHealth` to `true` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources.
- **Application and Network Load Balancers** : If you specify an ELB Application or Network Load Balancer and you set `EvaluateTargetHealth` to `true` , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer:
- For an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources.
- A target group that has no registered targets is considered unhealthy.

### Note

When you create a load balancer, you configure settings for Elastic Load Balancing health checks; theyâre not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer.

S3 buckets

There are no special requirements for setting `EvaluateTargetHealth` to `true` when the alias target is an S3 bucket.

Other records in the same hosted zone

If the Amazon Web Services resource that you specify in `DNSName` is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see [What Happens When You Omit Health Checks?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting) in the *Amazon Route 53 Developer Guide* .

For more information and examples, see [Amazon Route 53 Health Checks and DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) in the *Amazon Route 53 Developer Guide* .

HealthCheckId -> (string)

If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the `HealthCheckId` element and specify the ID of the applicable health check.

Route 53 determines whether a resource record set is healthy based on one of the following:

- By periodically sending a request to the endpoint that is specified in the health check
- By aggregating the status of a specified group of health checks (calculated health checks)
- By determining the current state of a CloudWatch alarm (CloudWatch metric health checks)

### Warning

Route 53 doesnât check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the `Value` element. When you add a `HealthCheckId` element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check.

For more information, see the following topics in the *Amazon Route 53 Developer Guide* :

- [How Amazon Route 53 Determines Whether an Endpoint Is Healthy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html)
- [Route 53 Health Checks and DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
- [Configuring Failover in a Private Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html)

**When to Specify HealthCheckId**

Specifying a value for `HealthCheckId` is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations:

- **Non-alias resource record sets** : Youâre checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets.  If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly.
- **Alias resource record sets** : You specify the following settings:
- You set `EvaluateTargetHealth` to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A).
- You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone.
- You specify a health check ID for the non-alias resource record set.

If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with.

If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set.

### Note

The alias resource record set can also route traffic to a *group* of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets.

**Geolocation Routing**

For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has `*` for `CountryCode` is `*` , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy:

- The United States
- North America
- The default resource record set

**Specifying the Health Check Endpoint by Domain Name**

If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each `HTTP` server that is serving content for `www.example.com` . For the value of `FullyQualifiedDomainName` , specify the domain name of the server (such as `us-east-2-www.example.com` ), not the name of the resource record sets (`www.example.com` ).

### Warning

Health check results will be unpredictable if you do the following:

- Create a health check that has the same value for `FullyQualifiedDomainName` as the name of a resource record set.
- Associate that health check with the resource record set.

TrafficPolicyInstanceId -> (string)

When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. `TrafficPolicyInstanceId` is the ID of the traffic policy instance that Route 53 created this resource record set for.

### Warning

To delete the resource record set that is associated with a traffic policy instance, use `DeleteTrafficPolicyInstance` . Route 53 will delete the resource record set automatically. If you delete the resource record set by using `ChangeResourceRecordSets` , Route 53 doesnât automatically delete the traffic policy instance, and youâll continue to be charged for it even though itâs no longer in use.

CidrRoutingConfig -> (structure)

The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.

A `LocationName` with an asterisk â*â can be used to create a default CIDR record. `CollectionId` is still required for default record.

CollectionId -> (string)

The CIDR collection ID.

LocationName -> (string)

The CIDR collection location name.

GeoProximityLocation -> (structure)

*GeoproximityLocation resource record sets only:* A complex type that lets you control how Route 53 responds to DNS queries based on the geographic origin of the query and your resources.

AWSRegion -> (string)

The Amazon Web Services Region the resource you are directing DNS traffic to, is in.

LocalZoneGroup -> (string)

Specifies an Amazon Web Services Local Zone Group.

A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is `us-east-1-bue-1a` the Local Zone Group is `us-east-1-bue-1` .

You can identify the Local Zones Group for a specific Local Zone by using the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) CLI command:

This command returns: `"GroupName": "us-west-2-den-1"` , specifying that the Local Zone `us-west-2-den-1a` belongs to the Local Zone Group `us-west-2-den-1` .

Coordinates -> (structure)

Contains the longitude and latitude for a geographic region.

Latitude -> (string)

Specifies a coordinate of the northâsouth position of a geographic point on the surface of the Earth (-90 - 90).

Longitude -> (string)

Specifies a coordinate of the eastâwest position of a geographic point on the surface of the Earth (-180 - 180).

Bias -> (integer)

The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource.

To use `Bias` to change the size of the geographic region, specify the applicable value for the bias:

- To expand the size of the geographic region from which Route 53 routes traffic to a resource, specify a positive integer from 1 to 99 for the bias. Route 53 shrinks the size of adjacent regions.
- To shrink the size of the geographic region from which Route 53 routes traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands the size of adjacent regions.

JSON Syntax:

```
{
  "Comment": "string",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "string",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"NAPTR"|"PTR"|"SRV"|"SPF"|"AAAA"|"CAA"|"DS"|"TLSA"|"SSHFP"|"SVCB"|"HTTPS",
        "SetIdentifier": "string",
        "Weight": long,
        "Region": "us-east-1"|"us-east-2"|"us-west-1"|"us-west-2"|"ca-central-1"|"eu-west-1"|"eu-west-2"|"eu-west-3"|"eu-central-1"|"eu-central-2"|"ap-southeast-1"|"ap-southeast-2"|"ap-southeast-3"|"ap-northeast-1"|"ap-northeast-2"|"ap-northeast-3"|"eu-north-1"|"sa-east-1"|"cn-north-1"|"cn-northwest-1"|"ap-east-1"|"me-south-1"|"me-central-1"|"ap-south-1"|"ap-south-2"|"af-south-1"|"eu-south-1"|"eu-south-2"|"ap-southeast-4"|"il-central-1"|"ca-west-1"|"ap-southeast-5"|"mx-central-1"|"ap-southeast-7"|"us-gov-east-1"|"us-gov-west-1",
        "GeoLocation": {
          "ContinentCode": "string",
          "CountryCode": "string",
          "SubdivisionCode": "string"
        },
        "Failover": "PRIMARY"|"SECONDARY",
        "MultiValueAnswer": true|false,
        "TTL": long,
        "ResourceRecords": [
          {
            "Value": "string"
          }
          ...
        ],
        "AliasTarget": {
          "HostedZoneId": "string",
          "DNSName": "string",
          "EvaluateTargetHealth": true|false
        },
        "HealthCheckId": "string",
        "TrafficPolicyInstanceId": "string",
        "CidrRoutingConfig": {
          "CollectionId": "string",
          "LocationName": "string"
        },
        "GeoProximityLocation": {
          "AWSRegion": "string",
          "LocalZoneGroup": "string",
          "Coordinates": {
            "Latitude": "string",
            "Longitude": "string"
          },
          "Bias": integer
        }
      }
    }
    ...
  ]
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

**To create, update, or delete a resource record set**

The following `change-resource-record-sets` command creates a resource record set using the `hosted-zone-id` `Z1R8UBAEXAMPLE` and the JSON-formatted configuration in the file `C:\awscli\route53\change-resource-record-sets.json`:

```
aws route53 change-resource-record-sets --hosted-zone-id Z1R8UBAEXAMPLE --change-batch file://C:\awscli\route53\change-resource-record-sets.json
```

For more information, see [POST ChangeResourceRecordSets](http://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) in the *Amazon Route 53 API Reference*.

The configuration in the JSON file depends on the kind of resource record set you want to create:

- Basic
- Weighted
- Alias
- Weighted Alias
- Latency
- Latency Alias
- Failover
- Failover Alias

**Basic Syntax**:

```
{
  "Comment": "optional comment about the changes in this change batch request",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "DNS domain name",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA",
        "TTL": time to live in seconds,
        "ResourceRecords": [
          {
            "Value": "applicable value for the record type"
          },
          {...}
        ]
      }
    },
    {...}
  ]
}
```

**Weighted Syntax**:

```
{
  "Comment": "optional comment about the changes in this change batch request",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "DNS domain name",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA",
        "SetIdentifier": "unique description for this resource record set",
        "Weight": value between 0 and 255,
        "TTL": time to live in seconds,
        "ResourceRecords": [
          {
            "Value": "applicable value for the record type"
          },
          {...}
        ],
        "HealthCheckId": "optional ID of an Amazon Route 53 health check"
      }
    },
    {...}
  ]
}
```

**Alias Syntax**:

```
{
  "Comment": "optional comment about the changes in this change batch request",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "DNS domain name",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA",
        "AliasTarget": {
          "HostedZoneId": "hosted zone ID for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or Amazon Route 53 hosted zone",
          "DNSName": "DNS domain name for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or another resource record set in this hosted zone",
          "EvaluateTargetHealth": true|false
        },
        "HealthCheckId": "optional ID of an Amazon Route 53 health check"
      }
    },
    {...}
  ]
}
```

**Weighted Alias Syntax**:

```
{
  "Comment": "optional comment about the changes in this change batch request",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "DNS domain name",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA",
        "SetIdentifier": "unique description for this resource record set",
        "Weight": value between 0 and 255,
        "AliasTarget": {
          "HostedZoneId": "hosted zone ID for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or Amazon Route 53 hosted zone",
          "DNSName": "DNS domain name for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or another resource record set in this hosted zone",
          "EvaluateTargetHealth": true|false
        },
        "HealthCheckId": "optional ID of an Amazon Route 53 health check"
      }
    },
    {...}
  ]
}
```

**Latency Syntax**:

```
{
  "Comment": "optional comment about the changes in this change batch request",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "DNS domain name",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA",
        "SetIdentifier": "unique description for this resource record set",
        "Region": "Amazon EC2 region name",
        "TTL": time to live in seconds,
        "ResourceRecords": [
          {
            "Value": "applicable value for the record type"
          },
          {...}
        ],
        "HealthCheckId": "optional ID of an Amazon Route 53 health check"
      }
    },
    {...}
  ]
}
```

**Latency Alias Syntax**:

```
{
  "Comment": "optional comment about the changes in this change batch request",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "DNS domain name",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA",
        "SetIdentifier": "unique description for this resource record set",
        "Region": "Amazon EC2 region name",
        "AliasTarget": {
          "HostedZoneId": "hosted zone ID for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or Amazon Route 53 hosted zone",
          "DNSName": "DNS domain name for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or another resource record set in this hosted zone",
          "EvaluateTargetHealth": true|false
        },
        "HealthCheckId": "optional ID of an Amazon Route 53 health check"
      }
    },
    {...}
  ]
}
```

**Failover Syntax**:

```
{
  "Comment": "optional comment about the changes in this change batch request",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "DNS domain name",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA",
        "SetIdentifier": "unique description for this resource record set",
        "Failover": "PRIMARY" | "SECONDARY",
        "TTL": time to live in seconds,
        "ResourceRecords": [
          {
            "Value": "applicable value for the record type"
          },
          {...}
        ],
        "HealthCheckId": "ID of an Amazon Route 53 health check"
      }
    },
    {...}
  ]
}
```

**Failover Alias Syntax**:

```
{
  "Comment": "optional comment about the changes in this change batch request",
  "Changes": [
    {
      "Action": "CREATE"|"DELETE"|"UPSERT",
      "ResourceRecordSet": {
        "Name": "DNS domain name",
        "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA",
        "SetIdentifier": "unique description for this resource record set",
        "Failover": "PRIMARY" | "SECONDARY",
        "AliasTarget": {
          "HostedZoneId": "hosted zone ID for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or Amazon Route 53 hosted zone",
          "DNSName": "DNS domain name for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or another resource record set in this hosted zone",
          "EvaluateTargetHealth": true|false
        },
        "HealthCheckId": "optional ID of an Amazon Route 53 health check"
      }
    },
    {...}
  ]
}
```

## Output

ChangeInfo -> (structure)

A complex type that contains information about changes made to your hosted zone.

This element contains an ID that you use when performing a [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) action to get detailed information about the change.

Id -> (string)

This element contains an ID that you use when performing a [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) action to get detailed information about the change.

Status -> (string)

The current state of the request. `PENDING` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt -> (timestamp)

The date and time that the change request was submitted in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) and Coordinated Universal Time (UTC). For example, the value `2017-03-27T17:48:16.751Z` represents March 27, 2017 at 17:48:16.751 UTC.

Comment -> (string)

A comment you can provide.