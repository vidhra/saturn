# gcloud recommender  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender](https://cloud.google.com/sdk/gcloud/reference/recommender)*

**NAME**

: **gcloud recommender - manage Cloud recommendations and recommendation rules**

**SYNOPSIS**

: **`gcloud recommender` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/recommender#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Recommender allows you to retrieve recommendations for Cloud resources, helping
you to improve security, save costs, and more. Each recommendation includes a
suggested action, its justification, and its impact. Recommendations are grouped
into a per-resource collection. To apply a recommendation, you must use the
desired service's API, not the Recommender. Interact with and manage resources
in Cloud Recommender.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[insight-type-config](https://cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config)`**:
Manage Cloud resource insight type configuration.

**`[insights](https://cloud.google.com/sdk/gcloud/reference/recommender/insights)`**:
Manage Cloud resource insights.

**`[recommendations](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations)`**:
Manage Cloud resource recommendations.

**`[recommender-config](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config)`**:
Manage Cloud resource recommender configuration.

**NOTES**

: These variants are also available:

```
gcloud alpha recommender
```

```
gcloud beta recommender
```