# describe-instance-typesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-types.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-types.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-instance-types

## Description

Describes the specified instance types. By default, all instance types for the current Region are described. Alternatively, you can filter the results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstanceTypes)

`describe-instance-types` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `InstanceTypes`

## Synopsis

```
describe-instance-types
[--dry-run | --no-dry-run]
[--instance-types <value>]
[--filters <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--instance-types` (list)

The instance types.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  a1.medium
  a1.large
  a1.xlarge
  a1.2xlarge
  a1.4xlarge
  a1.metal
  c1.medium
  c1.xlarge
  c3.large
  c3.xlarge
  c3.2xlarge
  c3.4xlarge
  c3.8xlarge
  c4.large
  c4.xlarge
  c4.2xlarge
  c4.4xlarge
  c4.8xlarge
  c5.large
  c5.xlarge
  c5.2xlarge
  c5.4xlarge
  c5.9xlarge
  c5.12xlarge
  c5.18xlarge
  c5.24xlarge
  c5.metal
  c5a.large
  c5a.xlarge
  c5a.2xlarge
  c5a.4xlarge
  c5a.8xlarge
  c5a.12xlarge
  c5a.16xlarge
  c5a.24xlarge
  c5ad.large
  c5ad.xlarge
  c5ad.2xlarge
  c5ad.4xlarge
  c5ad.8xlarge
  c5ad.12xlarge
  c5ad.16xlarge
  c5ad.24xlarge
  c5d.large
  c5d.xlarge
  c5d.2xlarge
  c5d.4xlarge
  c5d.9xlarge
  c5d.12xlarge
  c5d.18xlarge
  c5d.24xlarge
  c5d.metal
  c5n.large
  c5n.xlarge
  c5n.2xlarge
  c5n.4xlarge
  c5n.9xlarge
  c5n.18xlarge
  c5n.metal
  c6g.medium
  c6g.large
  c6g.xlarge
  c6g.2xlarge
  c6g.4xlarge
  c6g.8xlarge
  c6g.12xlarge
  c6g.16xlarge
  c6g.metal
  c6gd.medium
  c6gd.large
  c6gd.xlarge
  c6gd.2xlarge
  c6gd.4xlarge
  c6gd.8xlarge
  c6gd.12xlarge
  c6gd.16xlarge
  c6gd.metal
  c6gn.medium
  c6gn.large
  c6gn.xlarge
  c6gn.2xlarge
  c6gn.4xlarge
  c6gn.8xlarge
  c6gn.12xlarge
  c6gn.16xlarge
  c6i.large
  c6i.xlarge
  c6i.2xlarge
  c6i.4xlarge
  c6i.8xlarge
  c6i.12xlarge
  c6i.16xlarge
  c6i.24xlarge
  c6i.32xlarge
  c6i.metal
  cc1.4xlarge
  cc2.8xlarge
  cg1.4xlarge
  cr1.8xlarge
  d2.xlarge
  d2.2xlarge
  d2.4xlarge
  d2.8xlarge
  d3.xlarge
  d3.2xlarge
  d3.4xlarge
  d3.8xlarge
  d3en.xlarge
  d3en.2xlarge
  d3en.4xlarge
  d3en.6xlarge
  d3en.8xlarge
  d3en.12xlarge
  dl1.24xlarge
  f1.2xlarge
  f1.4xlarge
  f1.16xlarge
  g2.2xlarge
  g2.8xlarge
  g3.4xlarge
  g3.8xlarge
  g3.16xlarge
  g3s.xlarge
  g4ad.xlarge
  g4ad.2xlarge
  g4ad.4xlarge
  g4ad.8xlarge
  g4ad.16xlarge
  g4dn.xlarge
  g4dn.2xlarge
  g4dn.4xlarge
  g4dn.8xlarge
  g4dn.12xlarge
  g4dn.16xlarge
  g4dn.metal
  g5.xlarge
  g5.2xlarge
  g5.4xlarge
  g5.8xlarge
  g5.12xlarge
  g5.16xlarge
  g5.24xlarge
  g5.48xlarge
  g5g.xlarge
  g5g.2xlarge
  g5g.4xlarge
  g5g.8xlarge
  g5g.16xlarge
  g5g.metal
  hi1.4xlarge
  hpc6a.48xlarge
  hs1.8xlarge
  h1.2xlarge
  h1.4xlarge
  h1.8xlarge
  h1.16xlarge
  i2.xlarge
  i2.2xlarge
  i2.4xlarge
  i2.8xlarge
  i3.large
  i3.xlarge
  i3.2xlarge
  i3.4xlarge
  i3.8xlarge
  i3.16xlarge
  i3.metal
  i3en.large
  i3en.xlarge
  i3en.2xlarge
  i3en.3xlarge
  i3en.6xlarge
  i3en.12xlarge
  i3en.24xlarge
  i3en.metal
  im4gn.large
  im4gn.xlarge
  im4gn.2xlarge
  im4gn.4xlarge
  im4gn.8xlarge
  im4gn.16xlarge
  inf1.xlarge
  inf1.2xlarge
  inf1.6xlarge
  inf1.24xlarge
  is4gen.medium
  is4gen.large
  is4gen.xlarge
  is4gen.2xlarge
  is4gen.4xlarge
  is4gen.8xlarge
  m1.small
  m1.medium
  m1.large
  m1.xlarge
  m2.xlarge
  m2.2xlarge
  m2.4xlarge
  m3.medium
  m3.large
  m3.xlarge
  m3.2xlarge
  m4.large
  m4.xlarge
  m4.2xlarge
  m4.4xlarge
  m4.10xlarge
  m4.16xlarge
  m5.large
  m5.xlarge
  m5.2xlarge
  m5.4xlarge
  m5.8xlarge
  m5.12xlarge
  m5.16xlarge
  m5.24xlarge
  m5.metal
  m5a.large
  m5a.xlarge
  m5a.2xlarge
  m5a.4xlarge
  m5a.8xlarge
  m5a.12xlarge
  m5a.16xlarge
  m5a.24xlarge
  m5ad.large
  m5ad.xlarge
  m5ad.2xlarge
  m5ad.4xlarge
  m5ad.8xlarge
  m5ad.12xlarge
  m5ad.16xlarge
  m5ad.24xlarge
  m5d.large
  m5d.xlarge
  m5d.2xlarge
  m5d.4xlarge
  m5d.8xlarge
  m5d.12xlarge
  m5d.16xlarge
  m5d.24xlarge
  m5d.metal
  m5dn.large
  m5dn.xlarge
  m5dn.2xlarge
  m5dn.4xlarge
  m5dn.8xlarge
  m5dn.12xlarge
  m5dn.16xlarge
  m5dn.24xlarge
  m5dn.metal
  m5n.large
  m5n.xlarge
  m5n.2xlarge
  m5n.4xlarge
  m5n.8xlarge
  m5n.12xlarge
  m5n.16xlarge
  m5n.24xlarge
  m5n.metal
  m5zn.large
  m5zn.xlarge
  m5zn.2xlarge
  m5zn.3xlarge
  m5zn.6xlarge
  m5zn.12xlarge
  m5zn.metal
  m6a.large
  m6a.xlarge
  m6a.2xlarge
  m6a.4xlarge
  m6a.8xlarge
  m6a.12xlarge
  m6a.16xlarge
  m6a.24xlarge
  m6a.32xlarge
  m6a.48xlarge
  m6g.metal
  m6g.medium
  m6g.large
  m6g.xlarge
  m6g.2xlarge
  m6g.4xlarge
  m6g.8xlarge
  m6g.12xlarge
  m6g.16xlarge
  m6gd.metal
  m6gd.medium
  m6gd.large
  m6gd.xlarge
  m6gd.2xlarge
  m6gd.4xlarge
  m6gd.8xlarge
  m6gd.12xlarge
  m6gd.16xlarge
  m6i.large
  m6i.xlarge
  m6i.2xlarge
  m6i.4xlarge
  m6i.8xlarge
  m6i.12xlarge
  m6i.16xlarge
  m6i.24xlarge
  m6i.32xlarge
  m6i.metal
  mac1.metal
  p2.xlarge
  p2.8xlarge
  p2.16xlarge
  p3.2xlarge
  p3.8xlarge
  p3.16xlarge
  p3dn.24xlarge
  p4d.24xlarge
  r3.large
  r3.xlarge
  r3.2xlarge
  r3.4xlarge
  r3.8xlarge
  r4.large
  r4.xlarge
  r4.2xlarge
  r4.4xlarge
  r4.8xlarge
  r4.16xlarge
  r5.large
  r5.xlarge
  r5.2xlarge
  r5.4xlarge
  r5.8xlarge
  r5.12xlarge
  r5.16xlarge
  r5.24xlarge
  r5.metal
  r5a.large
  r5a.xlarge
  r5a.2xlarge
  r5a.4xlarge
  r5a.8xlarge
  r5a.12xlarge
  r5a.16xlarge
  r5a.24xlarge
  r5ad.large
  r5ad.xlarge
  r5ad.2xlarge
  r5ad.4xlarge
  r5ad.8xlarge
  r5ad.12xlarge
  r5ad.16xlarge
  r5ad.24xlarge
  r5b.large
  r5b.xlarge
  r5b.2xlarge
  r5b.4xlarge
  r5b.8xlarge
  r5b.12xlarge
  r5b.16xlarge
  r5b.24xlarge
  r5b.metal
  r5d.large
  r5d.xlarge
  r5d.2xlarge
  r5d.4xlarge
  r5d.8xlarge
  r5d.12xlarge
  r5d.16xlarge
  r5d.24xlarge
  r5d.metal
  r5dn.large
  r5dn.xlarge
  r5dn.2xlarge
  r5dn.4xlarge
  r5dn.8xlarge
  r5dn.12xlarge
  r5dn.16xlarge
  r5dn.24xlarge
  r5dn.metal
  r5n.large
  r5n.xlarge
  r5n.2xlarge
  r5n.4xlarge
  r5n.8xlarge
  r5n.12xlarge
  r5n.16xlarge
  r5n.24xlarge
  r5n.metal
  r6g.medium
  r6g.large
  r6g.xlarge
  r6g.2xlarge
  r6g.4xlarge
  r6g.8xlarge
  r6g.12xlarge
  r6g.16xlarge
  r6g.metal
  r6gd.medium
  r6gd.large
  r6gd.xlarge
  r6gd.2xlarge
  r6gd.4xlarge
  r6gd.8xlarge
  r6gd.12xlarge
  r6gd.16xlarge
  r6gd.metal
  r6i.large
  r6i.xlarge
  r6i.2xlarge
  r6i.4xlarge
  r6i.8xlarge
  r6i.12xlarge
  r6i.16xlarge
  r6i.24xlarge
  r6i.32xlarge
  r6i.metal
  t1.micro
  t2.nano
  t2.micro
  t2.small
  t2.medium
  t2.large
  t2.xlarge
  t2.2xlarge
  t3.nano
  t3.micro
  t3.small
  t3.medium
  t3.large
  t3.xlarge
  t3.2xlarge
  t3a.nano
  t3a.micro
  t3a.small
  t3a.medium
  t3a.large
  t3a.xlarge
  t3a.2xlarge
  t4g.nano
  t4g.micro
  t4g.small
  t4g.medium
  t4g.large
  t4g.xlarge
  t4g.2xlarge
  u-6tb1.56xlarge
  u-6tb1.112xlarge
  u-9tb1.112xlarge
  u-12tb1.112xlarge
  u-6tb1.metal
  u-9tb1.metal
  u-12tb1.metal
  u-18tb1.metal
  u-24tb1.metal
  vt1.3xlarge
  vt1.6xlarge
  vt1.24xlarge
  x1.16xlarge
  x1.32xlarge
  x1e.xlarge
  x1e.2xlarge
  x1e.4xlarge
  x1e.8xlarge
  x1e.16xlarge
  x1e.32xlarge
  x2iezn.2xlarge
  x2iezn.4xlarge
  x2iezn.6xlarge
  x2iezn.8xlarge
  x2iezn.12xlarge
  x2iezn.metal
  x2gd.medium
  x2gd.large
  x2gd.xlarge
  x2gd.2xlarge
  x2gd.4xlarge
  x2gd.8xlarge
  x2gd.12xlarge
  x2gd.16xlarge
  x2gd.metal
  z1d.large
  z1d.xlarge
  z1d.2xlarge
  z1d.3xlarge
  z1d.6xlarge
  z1d.12xlarge
  z1d.metal
  x2idn.16xlarge
  x2idn.24xlarge
  x2idn.32xlarge
  x2iedn.xlarge
  x2iedn.2xlarge
  x2iedn.4xlarge
  x2iedn.8xlarge
  x2iedn.16xlarge
  x2iedn.24xlarge
  x2iedn.32xlarge
  c6a.large
  c6a.xlarge
  c6a.2xlarge
  c6a.4xlarge
  c6a.8xlarge
  c6a.12xlarge
  c6a.16xlarge
  c6a.24xlarge
  c6a.32xlarge
  c6a.48xlarge
  c6a.metal
  m6a.metal
  i4i.large
  i4i.xlarge
  i4i.2xlarge
  i4i.4xlarge
  i4i.8xlarge
  i4i.16xlarge
  i4i.32xlarge
  i4i.metal
  x2idn.metal
  x2iedn.metal
  c7g.medium
  c7g.large
  c7g.xlarge
  c7g.2xlarge
  c7g.4xlarge
  c7g.8xlarge
  c7g.12xlarge
  c7g.16xlarge
  mac2.metal
  c6id.large
  c6id.xlarge
  c6id.2xlarge
  c6id.4xlarge
  c6id.8xlarge
  c6id.12xlarge
  c6id.16xlarge
  c6id.24xlarge
  c6id.32xlarge
  c6id.metal
  m6id.large
  m6id.xlarge
  m6id.2xlarge
  m6id.4xlarge
  m6id.8xlarge
  m6id.12xlarge
  m6id.16xlarge
  m6id.24xlarge
  m6id.32xlarge
  m6id.metal
  r6id.large
  r6id.xlarge
  r6id.2xlarge
  r6id.4xlarge
  r6id.8xlarge
  r6id.12xlarge
  r6id.16xlarge
  r6id.24xlarge
  r6id.32xlarge
  r6id.metal
  r6a.large
  r6a.xlarge
  r6a.2xlarge
  r6a.4xlarge
  r6a.8xlarge
  r6a.12xlarge
  r6a.16xlarge
  r6a.24xlarge
  r6a.32xlarge
  r6a.48xlarge
  r6a.metal
  p4de.24xlarge
  u-3tb1.56xlarge
  u-18tb1.112xlarge
  u-24tb1.112xlarge
  trn1.2xlarge
  trn1.32xlarge
  hpc6id.32xlarge
  c6in.large
  c6in.xlarge
  c6in.2xlarge
  c6in.4xlarge
  c6in.8xlarge
  c6in.12xlarge
  c6in.16xlarge
  c6in.24xlarge
  c6in.32xlarge
  m6in.large
  m6in.xlarge
  m6in.2xlarge
  m6in.4xlarge
  m6in.8xlarge
  m6in.12xlarge
  m6in.16xlarge
  m6in.24xlarge
  m6in.32xlarge
  m6idn.large
  m6idn.xlarge
  m6idn.2xlarge
  m6idn.4xlarge
  m6idn.8xlarge
  m6idn.12xlarge
  m6idn.16xlarge
  m6idn.24xlarge
  m6idn.32xlarge
  r6in.large
  r6in.xlarge
  r6in.2xlarge
  r6in.4xlarge
  r6in.8xlarge
  r6in.12xlarge
  r6in.16xlarge
  r6in.24xlarge
  r6in.32xlarge
  r6idn.large
  r6idn.xlarge
  r6idn.2xlarge
  r6idn.4xlarge
  r6idn.8xlarge
  r6idn.12xlarge
  r6idn.16xlarge
  r6idn.24xlarge
  r6idn.32xlarge
  c7g.metal
  m7g.medium
  m7g.large
  m7g.xlarge
  m7g.2xlarge
  m7g.4xlarge
  m7g.8xlarge
  m7g.12xlarge
  m7g.16xlarge
  m7g.metal
  r7g.medium
  r7g.large
  r7g.xlarge
  r7g.2xlarge
  r7g.4xlarge
  r7g.8xlarge
  r7g.12xlarge
  r7g.16xlarge
  r7g.metal
  c6in.metal
  m6in.metal
  m6idn.metal
  r6in.metal
  r6idn.metal
  inf2.xlarge
  inf2.8xlarge
  inf2.24xlarge
  inf2.48xlarge
  trn1n.32xlarge
  i4g.large
  i4g.xlarge
  i4g.2xlarge
  i4g.4xlarge
  i4g.8xlarge
  i4g.16xlarge
  hpc7g.4xlarge
  hpc7g.8xlarge
  hpc7g.16xlarge
  c7gn.medium
  c7gn.large
  c7gn.xlarge
  c7gn.2xlarge
  c7gn.4xlarge
  c7gn.8xlarge
  c7gn.12xlarge
  c7gn.16xlarge
  p5.48xlarge
  m7i.large
  m7i.xlarge
  m7i.2xlarge
  m7i.4xlarge
  m7i.8xlarge
  m7i.12xlarge
  m7i.16xlarge
  m7i.24xlarge
  m7i.48xlarge
  m7i-flex.large
  m7i-flex.xlarge
  m7i-flex.2xlarge
  m7i-flex.4xlarge
  m7i-flex.8xlarge
  m7a.medium
  m7a.large
  m7a.xlarge
  m7a.2xlarge
  m7a.4xlarge
  m7a.8xlarge
  m7a.12xlarge
  m7a.16xlarge
  m7a.24xlarge
  m7a.32xlarge
  m7a.48xlarge
  m7a.metal-48xl
  hpc7a.12xlarge
  hpc7a.24xlarge
  hpc7a.48xlarge
  hpc7a.96xlarge
  c7gd.medium
  c7gd.large
  c7gd.xlarge
  c7gd.2xlarge
  c7gd.4xlarge
  c7gd.8xlarge
  c7gd.12xlarge
  c7gd.16xlarge
  m7gd.medium
  m7gd.large
  m7gd.xlarge
  m7gd.2xlarge
  m7gd.4xlarge
  m7gd.8xlarge
  m7gd.12xlarge
  m7gd.16xlarge
  r7gd.medium
  r7gd.large
  r7gd.xlarge
  r7gd.2xlarge
  r7gd.4xlarge
  r7gd.8xlarge
  r7gd.12xlarge
  r7gd.16xlarge
  r7a.medium
  r7a.large
  r7a.xlarge
  r7a.2xlarge
  r7a.4xlarge
  r7a.8xlarge
  r7a.12xlarge
  r7a.16xlarge
  r7a.24xlarge
  r7a.32xlarge
  r7a.48xlarge
  c7i.large
  c7i.xlarge
  c7i.2xlarge
  c7i.4xlarge
  c7i.8xlarge
  c7i.12xlarge
  c7i.16xlarge
  c7i.24xlarge
  c7i.48xlarge
  mac2-m2pro.metal
  r7iz.large
  r7iz.xlarge
  r7iz.2xlarge
  r7iz.4xlarge
  r7iz.8xlarge
  r7iz.12xlarge
  r7iz.16xlarge
  r7iz.32xlarge
  c7a.medium
  c7a.large
  c7a.xlarge
  c7a.2xlarge
  c7a.4xlarge
  c7a.8xlarge
  c7a.12xlarge
  c7a.16xlarge
  c7a.24xlarge
  c7a.32xlarge
  c7a.48xlarge
  c7a.metal-48xl
  r7a.metal-48xl
  r7i.large
  r7i.xlarge
  r7i.2xlarge
  r7i.4xlarge
  r7i.8xlarge
  r7i.12xlarge
  r7i.16xlarge
  r7i.24xlarge
  r7i.48xlarge
  dl2q.24xlarge
  mac2-m2.metal
  i4i.12xlarge
  i4i.24xlarge
  c7i.metal-24xl
  c7i.metal-48xl
  m7i.metal-24xl
  m7i.metal-48xl
  r7i.metal-24xl
  r7i.metal-48xl
  r7iz.metal-16xl
  r7iz.metal-32xl
  c7gd.metal
  m7gd.metal
  r7gd.metal
  g6.xlarge
  g6.2xlarge
  g6.4xlarge
  g6.8xlarge
  g6.12xlarge
  g6.16xlarge
  g6.24xlarge
  g6.48xlarge
  gr6.4xlarge
  gr6.8xlarge
  c7i-flex.large
  c7i-flex.xlarge
  c7i-flex.2xlarge
  c7i-flex.4xlarge
  c7i-flex.8xlarge
  u7i-12tb.224xlarge
  u7in-16tb.224xlarge
  u7in-24tb.224xlarge
  u7in-32tb.224xlarge
  u7ib-12tb.224xlarge
  c7gn.metal
  r8g.medium
  r8g.large
  r8g.xlarge
  r8g.2xlarge
  r8g.4xlarge
  r8g.8xlarge
  r8g.12xlarge
  r8g.16xlarge
  r8g.24xlarge
  r8g.48xlarge
  r8g.metal-24xl
  r8g.metal-48xl
  mac2-m1ultra.metal
  g6e.xlarge
  g6e.2xlarge
  g6e.4xlarge
  g6e.8xlarge
  g6e.12xlarge
  g6e.16xlarge
  g6e.24xlarge
  g6e.48xlarge
  c8g.medium
  c8g.large
  c8g.xlarge
  c8g.2xlarge
  c8g.4xlarge
  c8g.8xlarge
  c8g.12xlarge
  c8g.16xlarge
  c8g.24xlarge
  c8g.48xlarge
  c8g.metal-24xl
  c8g.metal-48xl
  m8g.medium
  m8g.large
  m8g.xlarge
  m8g.2xlarge
  m8g.4xlarge
  m8g.8xlarge
  m8g.12xlarge
  m8g.16xlarge
  m8g.24xlarge
  m8g.48xlarge
  m8g.metal-24xl
  m8g.metal-48xl
  x8g.medium
  x8g.large
  x8g.xlarge
  x8g.2xlarge
  x8g.4xlarge
  x8g.8xlarge
  x8g.12xlarge
  x8g.16xlarge
  x8g.24xlarge
  x8g.48xlarge
  x8g.metal-24xl
  x8g.metal-48xl
  i7ie.large
  i7ie.xlarge
  i7ie.2xlarge
  i7ie.3xlarge
  i7ie.6xlarge
  i7ie.12xlarge
  i7ie.18xlarge
  i7ie.24xlarge
  i7ie.48xlarge
  i8g.large
  i8g.xlarge
  i8g.2xlarge
  i8g.4xlarge
  i8g.8xlarge
  i8g.12xlarge
  i8g.16xlarge
  i8g.24xlarge
  i8g.metal-24xl
  u7i-6tb.112xlarge
  u7i-8tb.112xlarge
  u7inh-32tb.480xlarge
  p5e.48xlarge
  p5en.48xlarge
  f2.12xlarge
  f2.48xlarge
  trn2.48xlarge
```

`--filters` (list)

One or more filters. Filter names and values are case-sensitive.

- `auto-recovery-supported` - Indicates whether Amazon CloudWatch action based recovery is supported (`true` | `false` ).
- `bare-metal` - Indicates whether it is a bare metal instance type (`true` | `false` ).
- `burstable-performance-supported` - Indicates whether the instance type is a burstable performance T instance type (`true` | `false` ).
- `current-generation` - Indicates whether this instance type is the latest generation instance type of an instance family (`true` | `false` ).
- `dedicated-hosts-supported` - Indicates whether the instance type supports Dedicated Hosts. (`true` | `false` )
- `ebs-info.ebs-optimized-info.baseline-bandwidth-in-mbps` - The baseline bandwidth performance for an EBS-optimized instance type, in Mbps.
- `ebs-info.ebs-optimized-info.baseline-iops` - The baseline input/output storage operations per second for an EBS-optimized instance type.
- `ebs-info.ebs-optimized-info.baseline-throughput-in-mbps` - The baseline throughput performance for an EBS-optimized instance type, in MB/s.
- `ebs-info.ebs-optimized-info.maximum-bandwidth-in-mbps` - The maximum bandwidth performance for an EBS-optimized instance type, in Mbps.
- `ebs-info.ebs-optimized-info.maximum-iops` - The maximum input/output storage operations per second for an EBS-optimized instance type.
- `ebs-info.ebs-optimized-info.maximum-throughput-in-mbps` - The maximum throughput performance for an EBS-optimized instance type, in MB/s.
- `ebs-info.ebs-optimized-support` - Indicates whether the instance type is EBS-optimized (`supported` | `unsupported` | `default` ).
- `ebs-info.encryption-support` - Indicates whether EBS encryption is supported (`supported` | `unsupported` ).
- `ebs-info.nvme-support` - Indicates whether non-volatile memory express (NVMe) is supported for EBS volumes (`required` | `supported` | `unsupported` ).
- `free-tier-eligible` - Indicates whether the instance type is eligible to use in the free tier (`true` | `false` ).
- `hibernation-supported` - Indicates whether On-Demand hibernation is supported (`true` | `false` ).
- `hypervisor` - The hypervisor (`nitro` | `xen` ).
- `instance-storage-info.disk.count` - The number of local disks.
- `instance-storage-info.disk.size-in-gb` - The storage size of each instance storage disk, in GB.
- `instance-storage-info.disk.type` - The storage technology for the local instance storage disks (`hdd` | `ssd` ).
- `instance-storage-info.encryption-support` - Indicates whether data is encrypted at rest (`required` | `supported` | `unsupported` ).
- `instance-storage-info.nvme-support` - Indicates whether non-volatile memory express (NVMe) is supported for instance store (`required` | `supported` | `unsupported` ).
- `instance-storage-info.total-size-in-gb` - The total amount of storage available from all local instance storage, in GB.
- `instance-storage-supported` - Indicates whether the instance type has local instance storage (`true` | `false` ).
- `instance-type` - The instance type (for example `c5.2xlarge` or c5*).
- `memory-info.size-in-mib` - The memory size.
- `network-info.bandwidth-weightings` - For instances that support bandwidth weighting to boost performance (`default` , `vpc-1` , `ebs-1` ).
- `network-info.efa-info.maximum-efa-interfaces` - The maximum number of Elastic Fabric Adapters (EFAs) per instance.
- `network-info.efa-supported` - Indicates whether the instance type supports Elastic Fabric Adapter (EFA) (`true` | `false` ).
- `network-info.ena-support` - Indicates whether Elastic Network Adapter (ENA) is supported or required (`required` | `supported` | `unsupported` ).
- `network-info.flexible-ena-queues-support` - Indicates whether an instance supports flexible ENA queues (`supported` | `unsupported` ).
- `network-info.encryption-in-transit-supported` - Indicates whether the instance type automatically encrypts in-transit traffic between instances (`true` | `false` ).
- `network-info.ipv4-addresses-per-interface` - The maximum number of private IPv4 addresses per network interface.
- `network-info.ipv6-addresses-per-interface` - The maximum number of private IPv6 addresses per network interface.
- `network-info.ipv6-supported` - Indicates whether the instance type supports IPv6 (`true` | `false` ).
- `network-info.maximum-network-cards` - The maximum number of network cards per instance.
- `network-info.maximum-network-interfaces` - The maximum number of network interfaces per instance.
- `network-info.network-performance` - The network performance (for example, â25 Gigabitâ).
- `nitro-enclaves-support` - Indicates whether Nitro Enclaves is supported (`supported` | `unsupported` ).
- `nitro-tpm-support` - Indicates whether NitroTPM is supported (`supported` | `unsupported` ).
- `nitro-tpm-info.supported-versions` - The supported NitroTPM version (`2.0` ).
- `processor-info.supported-architecture` - The CPU architecture (`arm64` | `i386` | `x86_64` ).
- `processor-info.sustained-clock-speed-in-ghz` - The CPU clock speed, in GHz.
- `processor-info.supported-features` - The supported CPU features (`amd-sev-snp` ).
- `reboot-migration-support` - Indicates whether enabling reboot migration is supported (`supported` | `unsupported` ).
- `supported-boot-mode` - The boot mode (`legacy-bios` | `uefi` ).
- `supported-root-device-type` - The root device type (`ebs` | `instance-store` ).
- `supported-usage-class` - The usage class (`on-demand` | `spot` | `capacity-block` ).
- `supported-virtualization-type` - The virtualization type (`hvm` | `paravirtual` ).
- `vcpu-info.default-cores` - The default number of cores for the instance type.
- `vcpu-info.default-threads-per-core` - The default number of threads per core for the instance type.
- `vcpu-info.default-vcpus` - The default number of vCPUs for the instance type.
- `vcpu-info.valid-cores` - The number of cores that can be configured for the instance type.
- `vcpu-info.valid-threads-per-core` - The number of threads per core that can be configured for the instance type. For example, â1â or â1,2â.

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

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

**Example 1: To describe an instance type**

The following `describe-instance-types` example displays details for the specified instance type.

```
aws ec2 describe-instance-types \
    --instance-types t2.micro
```

Output:

```
{
    "InstanceTypes": [
        {
            "InstanceType": "t2.micro",
            "CurrentGeneration": true,
            "FreeTierEligible": true,
            "SupportedUsageClasses": [
                "on-demand",
                "spot"
            ],
            "SupportedRootDeviceTypes": [
                "ebs"
            ],
            "BareMetal": false,
            "Hypervisor": "xen",
            "ProcessorInfo": {
                "SupportedArchitectures": [
                    "i386",
                    "x86_64"
                ],
                "SustainedClockSpeedInGhz": 2.5
            },
            "VCpuInfo": {
                "DefaultVCpus": 1,
                "DefaultCores": 1,
                "DefaultThreadsPerCore": 1,
                "ValidCores": [
                    1
                ],
                "ValidThreadsPerCore": [
                    1
                ]
            },
            "MemoryInfo": {
                "SizeInMiB": 1024
            },
            "InstanceStorageSupported": false,
            "EbsInfo": {
                "EbsOptimizedSupport": "unsupported",
                "EncryptionSupport": "supported"
            },
            "NetworkInfo": {
                "NetworkPerformance": "Low to Moderate",
                "MaximumNetworkInterfaces": 2,
                "Ipv4AddressesPerInterface": 2,
                "Ipv6AddressesPerInterface": 2,
                "Ipv6Supported": true,
                "EnaSupport": "unsupported"
            },
            "PlacementGroupInfo": {
                "SupportedStrategies": [
                    "partition",
                    "spread"
                ]
            },
            "HibernationSupported": false,
            "BurstablePerformanceSupported": true,
            "DedicatedHostsSupported": false,
            "AutoRecoverySupported": true
        }
    ]
}
```

For more information, see [Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in *Amazon Elastic Compute Cloud
User Guide for Linux Instances*.

**Example 2: To filter the available instance types**

You can specify a filter to scope the results to instance types that have a specific characteristic. The following `describe-instance-types` example lists the instance types that support hibernation.

```
aws ec2 describe-instance-types \
    --filters Name=hibernation-supported,Values=true --query 'InstanceTypes[*].InstanceType'
```

Output:

```
[
    "m5.8xlarge",
    "r3.large",
    "c3.8xlarge",
    "r5.large",
    "m4.4xlarge",
    "c4.large",
    "m5.xlarge",
    "m4.xlarge",
    "c3.large",
    "c4.8xlarge",
    "c4.4xlarge",
    "c5.xlarge",
    "c5.12xlarge",
    "r5.4xlarge",
    "c5.4xlarge"
]
```

For more information, see [Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in *Amazon Elastic Compute Cloud
User Guide for Linux Instances*.

## Output

InstanceTypes -> (list)

The instance type.

(structure)

Describes the instance type.

InstanceType -> (string)

The instance type. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

CurrentGeneration -> (boolean)

Indicates whether the instance type is current generation.

FreeTierEligible -> (boolean)

Indicates whether the instance type is eligible for the free tier.

SupportedUsageClasses -> (list)

Indicates whether the instance type is offered for spot, On-Demand, or Capacity Blocks.

(string)

SupportedRootDeviceTypes -> (list)

The supported root device types.

(string)

SupportedVirtualizationTypes -> (list)

The supported virtualization types.

(string)

BareMetal -> (boolean)

Indicates whether the instance is a bare metal instance type.

Hypervisor -> (string)

The hypervisor for the instance type.

ProcessorInfo -> (structure)

Describes the processor.

SupportedArchitectures -> (list)

The architectures supported by the instance type.

(string)

SustainedClockSpeedInGhz -> (double)

The speed of the processor, in GHz.

SupportedFeatures -> (list)

Indicates whether the instance type supports AMD SEV-SNP. If the request returns `amd-sev-snp` , AMD SEV-SNP is supported. Otherwise, it is not supported. For more information, see [AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html) .

(string)

Manufacturer -> (string)

The manufacturer of the processor.

VCpuInfo -> (structure)

Describes the vCPU configurations for the instance type.

DefaultVCpus -> (integer)

The default number of vCPUs for the instance type.

DefaultCores -> (integer)

The default number of cores for the instance type.

DefaultThreadsPerCore -> (integer)

The default number of threads per core for the instance type.

ValidCores -> (list)

The valid number of cores that can be configured for the instance type.

(integer)

ValidThreadsPerCore -> (list)

The valid number of threads per core that can be configured for the instance type.

(integer)

MemoryInfo -> (structure)

Describes the memory for the instance type.

SizeInMiB -> (long)

The size of the memory, in MiB.

InstanceStorageSupported -> (boolean)

Indicates whether instance storage is supported.

InstanceStorageInfo -> (structure)

Describes the instance storage for the instance type.

TotalSizeInGB -> (long)

The total size of the disks, in GB.

Disks -> (list)

Describes the disks that are available for the instance type.

(structure)

Describes a disk.

SizeInGB -> (long)

The size of the disk in GB.

Count -> (integer)

The number of disks with this configuration.

Type -> (string)

The type of disk.

NvmeSupport -> (string)

Indicates whether non-volatile memory express (NVMe) is supported.

EncryptionSupport -> (string)

Indicates whether data is encrypted at rest.

EbsInfo -> (structure)

Describes the Amazon EBS settings for the instance type.

EbsOptimizedSupport -> (string)

Indicates whether the instance type is Amazon EBS-optimized. For more information, see [Amazon EBS-optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) in *Amazon EC2 User Guide* .

EncryptionSupport -> (string)

Indicates whether Amazon EBS encryption is supported.

EbsOptimizedInfo -> (structure)

Describes the optimized EBS performance for the instance type.

BaselineBandwidthInMbps -> (integer)

The baseline bandwidth performance for an EBS-optimized instance type, in Mbps.

BaselineThroughputInMBps -> (double)

The baseline throughput performance for an EBS-optimized instance type, in MB/s.

BaselineIops -> (integer)

The baseline input/output storage operations per seconds for an EBS-optimized instance type.

MaximumBandwidthInMbps -> (integer)

The maximum bandwidth performance for an EBS-optimized instance type, in Mbps.

MaximumThroughputInMBps -> (double)

The maximum throughput performance for an EBS-optimized instance type, in MB/s.

MaximumIops -> (integer)

The maximum input/output storage operations per second for an EBS-optimized instance type.

NvmeSupport -> (string)

Indicates whether non-volatile memory express (NVMe) is supported.

NetworkInfo -> (structure)

Describes the network settings for the instance type.

NetworkPerformance -> (string)

The network performance.

MaximumNetworkInterfaces -> (integer)

The maximum number of network interfaces for the instance type.

MaximumNetworkCards -> (integer)

The maximum number of physical network cards that can be allocated to the instance.

DefaultNetworkCardIndex -> (integer)

The index of the default network card, starting at 0.

NetworkCards -> (list)

Describes the network cards for the instance type.

(structure)

Describes the network card support of the instance type.

NetworkCardIndex -> (integer)

The index of the network card.

NetworkPerformance -> (string)

The network performance of the network card.

MaximumNetworkInterfaces -> (integer)

The maximum number of network interfaces for the network card.

BaselineBandwidthInGbps -> (double)

The baseline network performance of the network card, in Gbps.

PeakBandwidthInGbps -> (double)

The peak (burst) network performance of the network card, in Gbps.

DefaultEnaQueueCountPerInterface -> (integer)

The default number of the ENA queues for each interface.

MaximumEnaQueueCount -> (integer)

The maximum number of the ENA queues.

MaximumEnaQueueCountPerInterface -> (integer)

The maximum number of the ENA queues for each interface.

Ipv4AddressesPerInterface -> (integer)

The maximum number of IPv4 addresses per network interface.

Ipv6AddressesPerInterface -> (integer)

The maximum number of IPv6 addresses per network interface.

Ipv6Supported -> (boolean)

Indicates whether IPv6 is supported.

EnaSupport -> (string)

Indicates whether Elastic Network Adapter (ENA) is supported.

EfaSupported -> (boolean)

Indicates whether Elastic Fabric Adapter (EFA) is supported.

EfaInfo -> (structure)

Describes the Elastic Fabric Adapters for the instance type.

MaximumEfaInterfaces -> (integer)

The maximum number of Elastic Fabric Adapters for the instance type.

EncryptionInTransitSupported -> (boolean)

Indicates whether the instance type automatically encrypts in-transit traffic between instances.

EnaSrdSupported -> (boolean)

Indicates whether the instance type supports ENA Express. ENA Express uses Amazon Web Services Scalable Reliable Datagram (SRD) technology to increase the maximum bandwidth used per stream and minimize tail latency of network traffic between EC2 instances.

BandwidthWeightings -> (list)

A list of valid settings for configurable bandwidth weighting for the instance type, if supported.

(string)

FlexibleEnaQueuesSupport -> (string)

Indicates whether changing the number of ENA queues is supported.

GpuInfo -> (structure)

Describes the GPU accelerator settings for the instance type.

Gpus -> (list)

Describes the GPU accelerators for the instance type.

(structure)

Describes the GPU accelerators for the instance type.

Name -> (string)

The name of the GPU accelerator.

Manufacturer -> (string)

The manufacturer of the GPU accelerator.

Count -> (integer)

The number of GPUs for the instance type.

MemoryInfo -> (structure)

Describes the memory available to the GPU accelerator.

SizeInMiB -> (integer)

The size of the memory available to the GPU accelerator, in MiB.

TotalGpuMemoryInMiB -> (integer)

The total size of the memory for the GPU accelerators for the instance type, in MiB.

FpgaInfo -> (structure)

Describes the FPGA accelerator settings for the instance type.

Fpgas -> (list)

Describes the FPGAs for the instance type.

(structure)

Describes the FPGA accelerator for the instance type.

Name -> (string)

The name of the FPGA accelerator.

Manufacturer -> (string)

The manufacturer of the FPGA accelerator.

Count -> (integer)

The count of FPGA accelerators for the instance type.

MemoryInfo -> (structure)

Describes the memory for the FPGA accelerator for the instance type.

SizeInMiB -> (integer)

The size of the memory available to the FPGA accelerator, in MiB.

TotalFpgaMemoryInMiB -> (integer)

The total memory of all FPGA accelerators for the instance type.

PlacementGroupInfo -> (structure)

Describes the placement group settings for the instance type.

SupportedStrategies -> (list)

The supported placement group types.

(string)

InferenceAcceleratorInfo -> (structure)

Describes the Inference accelerator settings for the instance type.

Accelerators -> (list)

Describes the Inference accelerators for the instance type.

(structure)

### Note

Amazon Elastic Inference is no longer available.

Describes the Inference accelerators for the instance type.

Count -> (integer)

The number of Inference accelerators for the instance type.

Name -> (string)

The name of the Inference accelerator.

Manufacturer -> (string)

The manufacturer of the Inference accelerator.

MemoryInfo -> (structure)

Describes the memory available to the inference accelerator.

SizeInMiB -> (integer)

The size of the memory available to the inference accelerator, in MiB.

TotalInferenceMemoryInMiB -> (integer)

The total size of the memory for the inference accelerators for the instance type, in MiB.

HibernationSupported -> (boolean)

Indicates whether On-Demand hibernation is supported.

BurstablePerformanceSupported -> (boolean)

Indicates whether the instance type is a burstable performance T instance type. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) .

DedicatedHostsSupported -> (boolean)

Indicates whether Dedicated Hosts are supported on the instance type.

AutoRecoverySupported -> (boolean)

Indicates whether Amazon CloudWatch action based recovery is supported.

SupportedBootModes -> (list)

The supported boot modes. For more information, see [Boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide* .

(string)

NitroEnclavesSupport -> (string)

Indicates whether Nitro Enclaves is supported.

NitroTpmSupport -> (string)

Indicates whether NitroTPM is supported.

NitroTpmInfo -> (structure)

Describes the supported NitroTPM versions for the instance type.

SupportedVersions -> (list)

Indicates the supported NitroTPM versions.

(string)

MediaAcceleratorInfo -> (structure)

Describes the media accelerator settings for the instance type.

Accelerators -> (list)

Describes the media accelerators for the instance type.

(structure)

Describes the media accelerators for the instance type.

Count -> (integer)

The number of media accelerators for the instance type.

Name -> (string)

The name of the media accelerator.

Manufacturer -> (string)

The manufacturer of the media accelerator.

MemoryInfo -> (structure)

Describes the memory available to the media accelerator.

SizeInMiB -> (integer)

The size of the memory available to each media accelerator, in MiB.

TotalMediaMemoryInMiB -> (integer)

The total size of the memory for the media accelerators for the instance type, in MiB.

NeuronInfo -> (structure)

Describes the Neuron accelerator settings for the instance type.

NeuronDevices -> (list)

Describes the neuron accelerators for the instance type.

(structure)

Describes the neuron accelerators for the instance type.

Count -> (integer)

The number of neuron accelerators for the instance type.

Name -> (string)

The name of the neuron accelerator.

CoreInfo -> (structure)

Describes the cores available to each neuron accelerator.

Count -> (integer)

The number of cores available to the neuron accelerator.

Version -> (integer)

The version of the neuron accelerator.

MemoryInfo -> (structure)

Describes the memory available to each neuron accelerator.

SizeInMiB -> (integer)

The size of the memory available to the neuron accelerator, in MiB.

TotalNeuronDeviceMemoryInMiB -> (integer)

The total size of the memory for the neuron accelerators for the instance type, in MiB.

PhcSupport -> (string)

Indicates whether a local Precision Time Protocol (PTP) hardware clock (PHC) is supported.

RebootMigrationSupport -> (string)

Indicates whether reboot migration during a user-initiated reboot is supported for instances that have a scheduled `system-reboot` event. For more information, see [Enable or disable reboot migration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration) in the *Amazon EC2 User Guide* .

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.