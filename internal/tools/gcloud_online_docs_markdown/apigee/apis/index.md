# gcloud apigee apis  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee/apis](https://cloud.google.com/sdk/gcloud/reference/apigee/apis)*

**NAME**

: **gcloud apigee apis - manage Apigee API proxies**

**SYNOPSIS**

: **`gcloud apigee apis` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/apigee/apis#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee/apis#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Apigee API proxies.

**EXAMPLES**

: To list all the API proxies in the active Cloud Platform project, run:

```
gcloud apigee apis list
```

To get details about a specific API proxy in a specific Apigee organization,
run:

```
gcloud apigee apis describe PROXY_NAME --organization=ORG_NAME
```

To get a JSON object containing revision-level details about an API proxy, run:

```
gcloud apigee apis describe PROXY_NAME --verbose --format=json
```

To deploy the most recent revision of an API proxy into the
``eval`` deployment environment, run:

```
gcloud apigee apis deploy --api=PROXY_NAME --environment=eval
```

To deploy the first revision of that API proxy into the
``release`` deployment environment, run:

```
gcloud apigee apis deploy 1 --api=PROXY_NAME --environment=release
```

To undeploy whatever revision of PROXY_NAME is currently deployed in
ENVIRONMENT, run:

```
gcloud apigee apis undeploy --api=PROXY_NAME --environment=ENVIRONMENT
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/deploy)`**:
Deploy an API proxy to an environment.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/describe)`**:
Describe an Apigee API proxy.

**`[list](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/list)`**:
List Apigee API proxies.

**`[undeploy](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy)`**:
Undeploy an Apigee API proxy from an environment.

**NOTES**

: These variants are also available:

```
gcloud alpha apigee apis
```

```
gcloud beta apigee apis
```