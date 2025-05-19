# gcloud compute security-policies add-layer7-ddos-defense-threshold-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config)*

**NAME**

: **gcloud compute security-policies add-layer7-ddos-defense-threshold-config - add a layer7 ddos defense threshold config to a Compute Engine security policy**

**SYNOPSIS**

: **`gcloud compute security-policies add-layer7-ddos-defense-threshold-config` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#NAME)` `[--threshold-config-name](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--threshold-config-name)`=`THRESHOLD_CONFIG_NAME` [`[--auto-deploy-confidence-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--auto-deploy-confidence-threshold)`=`AUTO_DEPLOY_CONFIDENCE_THRESHOLD`] [`[--auto-deploy-expiration-sec](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--auto-deploy-expiration-sec)`=`AUTO_DEPLOY_EXPIRATION_SEC`] [`[--auto-deploy-impacted-baseline-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--auto-deploy-impacted-baseline-threshold)`=`AUTO_DEPLOY_IMPACTED_BASELINE_THRESHOLD`] [`[--auto-deploy-load-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--auto-deploy-load-threshold)`=`AUTO_DEPLOY_LOAD_THRESHOLD`] [`[--detection-absolute-qps](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--detection-absolute-qps)`=`DETECTION_ABSOLUTE_QPS`] [`[--detection-load-threshold](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--detection-load-threshold)`=`DETECTION_LOAD_THRESHOLD`] [`[--detection-relative-to-baseline-qps](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--detection-relative-to-baseline-qps)`=`DETECTION_RELATIVE_TO_BASELINE_QPS`] [`[--traffic-granularity-configs](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#--traffic-granularity-configs)`=[`type`=`TYPE`[,`value`=`VALUE`][,`enableEachUniqueValue`=`ENABLE_EACH_UNIQUE_VALUE`];…;…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies
add-layer7-ddos-defense-threshold-config` is used to add layer7 ddos
defense threshold configs to security policies.

**EXAMPLES**

: To add a layer7 ddos defense threshold config run the following command:

```
gcloud compute security-policies add-layer7-ddos-defense-threshold-config NAME --threshold-config-name=my-threshold-config-name --auto-deploy-load-threshold=0.7 --auto-deploy-confidence-threshold=0.8 --auto-deploy-impacted-baseline-threshold=0.1 --auto-deploy-expiration-sec=4800 --detection-load-threshold=0.4 --detection-absolute-qps=1000 --detection-relative-to-baseline-qps=2.0 --traffic-granularity-configs=type=HTTP_HEADER_HOST,value=www.my-test-host.com;type=HTTP_PATH,enableEachUniqueValue=true
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the security policy to update.

**REQUIRED FLAGS**

: **--threshold-config-name**:
The name for the threshold config.

**OPTIONAL FLAGS**

: **--auto-deploy-confidence-threshold**:
The threshold of the confidence of an identified attack, over which auto-deploy
takes action.

**--auto-deploy-expiration-sec**:
The duration of actions, if any, taken by auto-deploy.

**--auto-deploy-impacted-baseline-threshold**:
The threshold on the estimated impact to the baseline traffic of a suggested
mitigation, below which auto-deploy takes action.

**--auto-deploy-load-threshold**:
The threshold on backend's load, over which auto-deploy takes action.

**--detection-absolute-qps**:
The absolute QPS of the incoming traffic, over which adaptive protection detects
an attack.

**--detection-load-threshold**:
The threshold on backend's load, over which adaptive protection detects an
attack.

**--detection-relative-to-baseline-qps**:
The QPS of the incoming traffic relative to the average baseline QPS, over which
adaptive protection detects an attack.

**--traffic-granularity-configs**:
Specify up to 2 configs matching a specifc type/value of traffic.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha compute security-policies add-layer7-ddos-defense-threshold-config
```

```
gcloud beta compute security-policies add-layer7-ddos-defense-threshold-config
```