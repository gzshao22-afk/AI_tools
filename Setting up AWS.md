1. Account Lockdown (Day 1)

- **Secure Root:** Log in with your email and immediately enable **MFA** (Multi-Factor Authentication).
- **Create an Admin User:** Follow the **IAM** steps discussed earlier: create an "Admin" group with `AdministratorAccess`, add a new user to it, and then **log out of Root** forever.
- **Set a Billing Alarm:** Go to the Billing Dashboard and create a "CloudWatch Alarm" to email you if your monthly spend exceeds a small amount (e.g., $5). This protects you from accidental "bill shock."

2. Networking Setup (The "House")

- **VPC (Virtual Private Cloud):** AWS gives you a "Default VPC," but for real work, you should understand subnets.
- **Public vs. Private:** Decide which resources need to be on the internet (Public Subnet) and which should be hidden (Private Subnet).
- **Security Groups:** Set up these virtual firewalls to only allow specific traffic (e.g., only your IP address can SSH into your servers).

3. Compute & Storage (The "Furniture")

- **EC2 or Containers:** Launch an **EC2** instance for a raw VM, or set up **ECS/Fargate** if you are using Docker.
- **Storage Strategy:** Choose **EBS** for a single server's "hard drive" or **EFS** if you need an "elastic" file system shared across multiple servers.
- **S3 Buckets:** Create an S3 bucket for any "Object" storage (images, backups, or static website files).

4. Application Management

- **Dockerize:** Package your app in a **Docker** container to ensure it works on AWS exactly like it did on your laptop.
- **Load Balancing:** Set up an **Application Load Balancer (ALB)** to sit in front of your servers, handle SSL certificates (HTTPS), and distribute traffic.
- **Infrastructure as Code (IaC):** As you get more advanced, use **Terraform** or **AWS CloudFormation** to "write" your infrastructure as code instead of clicking buttons in the console.

5. Access & CLI

- **Install AWS CLI:** Download the command-line tool on your local machine and run `aws configure` using the **Access Keys** from your IAM user. This lets you manage AWS without the browser.