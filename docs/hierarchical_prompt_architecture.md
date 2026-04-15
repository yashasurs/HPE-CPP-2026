# Hierarchical Prompt Architecture

## 1. Overview
This document defines the static context loading strategy for the compressed AWS knowledge base. Because we cannot fit the entirety of AWS documentation into a single prompt without degrading reasoning quality and exceeding context windows, the compressed knowledge is structured into three distinct layers.

This architecture guarantees that the LLM always has the required foundational context (Layer 0), while dynamically appending deeper domain knowledge (Layer 1) and niche topics (Layer 2) strictly based on the user's query intent.

This approach prevents context dilution and ensures the model reasons over relevant, high-signal, low-redundancy information within token constraints.

---

## 2. Layer 0: The Core Snapshot (Always Loaded)

**Token Budget:** ~500 – 1000 tokens  
**Loading Trigger:** Always Active (Injected into base system prompt)  
**Target Services:** EC2, S3, IAM, VPC, Lambda  

---

### Specification

Layer 0 is **not** a collection of summaries. It is a **dense, cross-linked snapshot** of foundational AWS primitives and their interactions. It defines the “laws of physics” of the AWS ecosystem.

---

### Structure (Strict)

Each Layer 0 block must follow:

- **Entities** → Core services (EC2, S3, IAM, VPC, Lambda)  
- **Relationships** → Explicit service interactions  
- **Constraints** → Hard limits and defaults  
- **Scope** → Global vs regional behavior  

---

### Content to Include

#### 1. Key Interconnections (The Web)

- Lambda executes within a VPC, uses IAM roles, and can be triggered by S3 events  
- EC2 runs inside VPC subnets, uses EBS for storage, and IAM roles for access  
- IAM governs permissions across ALL services  
- S3 acts as shared storage accessed by EC2 and Lambda  
- VPC defines network boundaries and connectivity  

---

#### 2. Critical Limits & Defaults

- Lambda → 15-minute timeout, 10GB memory  
- S3 → 5TB object size, private by default  
- VPC → Max 5 CIDR blocks, ~5 VPCs per region (default limit)  

---

#### 3. Global vs Regional Scope

- IAM → Global  
- EC2, VPC, Lambda → Regional  
- S3 → Global namespace, regionally stored  

---

### Constraints (Strict Rules)

Layer 0 must NOT contain:
- Step-by-step procedures  
- Configuration instructions  
- Deep service-specific implementation details  

All statements must be derived from validated atomic knowledge units (AKUs).

---

## 3. Layer 1: Domain-Specific Blocks (Loaded by Intent)

**Token Budget:** ~2000 – 3000 tokens per domain  
**Loading Trigger:** Intent Classification (Query Mapping)  

---

### Supported Domains

- **Database Domain:** Amazon RDS, DynamoDB  
- **Infrastructure as Code (IaC):** AWS CloudFormation  
- **Observability Domain:** CloudWatch, CloudTrail  

---

### Specification

Layer 1 blocks contain compressed domain knowledge extracted from the pipeline.

- Multiple Layer 1 domains can be loaded if required  
- Soft cap: **2–3 domains maximum** to maintain efficiency  

---

### Query → Domain Mapping

#### 1. Keyword Heuristics
- "RDS", "PostgreSQL", "Aurora" → Database Domain  
- "CloudFormation", "template", "stack" → IaC Domain  

#### 2. Semantic Intent
- "monitor", "logs", "metrics" → Observability Domain  

#### 3. Operational Context
- "deploy", "rollback", "automation" → IaC Domain  

---

### Priority Rule


Explicit Service Mention > Semantic Intent > Inferred Context


---

### Loading Behavior

If a domain is triggered, the corresponding compressed `.md` block is appended as a **Layer 1 context block**.

---

## 4. Layer 2: On-Demand Topics (Triggered by Entity)
**Loading Trigger:** Entity Detection (Exact + Semantic Match)  

---

### Target Services

ECS, API Gateway, Step Functions, Kinesis, EventBridge, etc.

---

### Specification

Layer 2 contains highly specific service-level knowledge. These are loaded only when explicitly required.

---

### Trigger Mechanism

#### 1. Exact Match
- "API Gateway" → load `api_gateway.md`  
- "Kinesis" → load `kinesis.md`  

#### 2. Semantic Match
- "API endpoints" → API Gateway  
- "real-time streaming" → Kinesis  

---

### Stacking Behavior

- Multiple Layer 2 topics can be loaded  
- Example:

"Connect API Gateway to Step Functions"
→ Load both topics


---

### Token Guard

Maximum of **2–3 Layer 2 topics** can be loaded simultaneously to prevent overflow.

---

### Fallback

If no entities are detected, Layer 2 is skipped entirely.

---

## 5. Assembly Example
### User Query

> "How do I deploy an RDS Postgres database using CloudFormation and monitor its CPU?"

---

### Context Assembly

1. **Layer 0**  
 Base primitives: IAM permissions, VPC networking for RDS  
 

2. **Layer 1 – IaC Domain**  
 CloudFormation templates, stack lifecycle, rollback logic  
 

3. **Layer 1 – Database Domain**  
 RDS PostgreSQL configuration, scaling, networking  
 

4. **Layer 1 – Observability Domain**  
 CloudWatch metrics, alarms, CPU monitoring  
 

5. **Layer 2**  
 Not triggered (if enough context is provided at the above layers itself)
 

---

### Why Multiple Domains?

The query spans:
- Deployment → IaC Domain  
- Database setup → Database Domain  
- Monitoring → Observability Domain  

---
This ensures:
- High relevance  
- Minimal noise  
- Maximum reasoning headroom  

---

## 6. Key Design Principles

### 1. Minimal Token Usage
Load only what is required

### 2. Maximum Context Relevance
Prioritize high-signal knowledge

### 3. Strong Interconnections
Services are modeled as a system, not isolated components

### 4. Layered Reasoning
- Layer 0 → System invariants  
- Layer 1 → Domain intelligence  
- Layer 2 → Task-specific precision  

---

## 7. Final Insight

This architecture transforms prompting from:

Flat context dumping into a Structured, layered knowledge injection.

It functions as:

> A context-aware reasoning system rather than a static prompt

---