# Vidhra
Better management, finops, and usage of cloud

### Overview
Vidhra is a Cloud Wastage Reduction Tool, an open-source project designed to efficiently manage cloud resources, reduce cloud wastage, and optimize costs. It includes a **Karma Allocation** inspired by the paper [karma allocator](https://www.usenix.org/conference/osdi23/presentation/vuppalapati) module to allocate cloud resources based on usage efficiency and a **FinOps** module to provide optimization recommendations, generate reports, and manage cloud wastage alerts.

The project integrates with **AWS** and **GCP** billing APIs to track cloud costs, provide actionable optimization suggestions, and reward efficient teams with monetary credits. The Karma allocator encourages teams to be more resource-efficient, while the FinOps module helps organizations take control of their cloud spending.

### Features
- **Karma Allocation**: Allocates cloud resources to teams based on efficiency, rewarding optimal usage.
- **FinOps Optimization**: Detects cloud wastage and provides optimization recommendations to reduce costs.
- **Cloud Integration**: Integrates with AWS and GCP billing APIs for real-time cost monitoring.
- **Cost Reporting**: Generates detailed reports on cloud costs, efficiency, and areas for potential savings.
- **Alert System**: Sets alerts for inefficient cloud usage, budget overruns, and underutilized resources.
- **Gamification**: A Karma credit system motivates teams to improve cloud resource management.
### Leveraging LLMs for Enhanced Functionality

**Vidhra** uses **Large Language Models (LLMs)** to make data processing, reporting, and decision-making more efficient. Here’s how LLMs are utilized to simplify and enhance various aspects of the project:

1. **Data Fetching and Analysis**:
   LLMs can be integrated to parse and analyze cloud usage data fetched from **AWS** and **GCP**. They provide natural language insights, identify underutilized resources, predict peak demands, and detect anomalies more effectively.
   - Example Prompt: `"Analyze patterns and suggest areas where resources can be optimized."`

2. **Natural Language Reporting**:
   - The **FinOps Reporting Module** leverages LLMs to generate easy-to-understand reports summarizing cost-saving opportunities, wastage trends, and recommendations for each team.
   - These reports can be customized by querying the LLM in natural language, such as: `"Generate a report showing the top 5 optimization opportunities for the month."`

3. **Real-Time Recommendations**:
   LLMs can provide real-time optimization suggestions by continuously analyzing cloud metrics and identifying potential issues. They detect scenarios such as overprovisioning or idle instances and generate suggestions to either scale down resources or move to a different instance type.
   - Example: "Consider switching this instance to a spot instance to save 30% in costs."

4. **Automated Alert Messaging**:
   - The **Alerts Module** is enhanced with LLMs to formulate alert messages in natural language, making it easier for DevOps teams to understand and act upon. Instead of raw metrics, alerts will include explanations like: "The resource utilization, for instance, XYZ, has dropped below 10% for the last 48 hours. Consider rightsizing or shutting it down."

5. **Interactive Querying**:
   - LLMs enable users to query cloud cost data and optimization opportunities interactively. Users can ask questions like: "Which department has the highest cloud wastage?" and receive a detailed response, along with suggestions for improvement.

6. **Simplified Integration**:
   - By using LLMs, integration with **AWS** and **GCP** billing APIs becomes more intuitive. LLMs help generate API requests or Terraform configurations, allowing the tool to scale or provision cloud resources based on natural language instructions.
