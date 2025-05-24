# codeguruprofilerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# codeguruprofiler

## Description

This section provides documentation for the Amazon CodeGuru Profiler API operations.

Amazon CodeGuru Profiler collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance. Using machine learning algorithms, CodeGuru Profiler can help you find your most expensive lines of code and suggest ways you can improve efficiency and remove CPU bottlenecks.

Amazon CodeGuru Profiler provides different visualizations of profiling data to help you identify what code is running on the CPU, see how much time is consumed, and suggest ways to reduce CPU utilization.

### Note

Amazon CodeGuru Profiler currently supports applications written in all Java virtual machine (JVM) languages and Python. While CodeGuru Profiler supports both visualizations and recommendations for applications written in Java, it can also generate visualizations and a subset of recommendations for applications written in other JVM languages and Python.

For more information, see [What is Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html) in the *Amazon CodeGuru Profiler User Guide* .

## Available Commands

- [add-notification-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/add-notification-channels.html)
- [batch-get-frame-metric-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/batch-get-frame-metric-data.html)
- [configure-agent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/configure-agent.html)
- [create-profiling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/create-profiling-group.html)
- [delete-profiling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/delete-profiling-group.html)
- [describe-profiling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/describe-profiling-group.html)
- [get-findings-report-account-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/get-findings-report-account-summary.html)
- [get-notification-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/get-notification-configuration.html)
- [get-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/get-policy.html)
- [get-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/get-profile.html)
- [get-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/get-recommendations.html)
- [list-findings-reports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-findings-reports.html)
- [list-profile-times](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-profile-times.html)
- [list-profiling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-profiling-groups.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-tags-for-resource.html)
- [post-agent-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/post-agent-profile.html)
- [put-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/put-permission.html)
- [remove-notification-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/remove-notification-channel.html)
- [remove-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/remove-permission.html)
- [submit-feedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/submit-feedback.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/untag-resource.html)
- [update-profiling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/update-profiling-group.html)