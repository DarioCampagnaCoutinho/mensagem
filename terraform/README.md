Terraform para deploy da aplicação `mensagem` em ECS Fargate.

Arquivos principais:
- `provider.tf` - provider AWS
- `variables.tf` - variáveis padrão (região, CIDRs, tags)
- `vpc.tf` - VPC, subnets públicas/privadas e IGW
- `sg.tf` - security groups para ALB e ECS tasks
- `alb.tf` - Application Load Balancer e target group
- `ecr.tf` - ECR repository
- `logs.tf` - CloudWatch Log Group
- `iam.tf` - roles/permissions para ECS task execution
- `secrets.tf` - Secrets Manager secret (exemplo)
- `ecs_cluster.tf` - ECS cluster
- `ecs_task.tf` - Task definition (container definitions usando ECR image)
- `ecs_service.tf` - ECS service (Fargate) ligado ao ALB
- `certificate.tf` - ACM certificate (comentado por padrão)

Instruções rápidas:
1. Configure as credenciais AWS (ex: AWS_PROFILE ou variáveis de ambiente)
2. Edite `terraform/variables.tf` conforme necessário (CIDRs, região)
3. `terraform init && terraform apply` (recomendo revisar o plano antes)

Notas:
- O recurso ACM está presente, mas comentado; habilite manualmente e forneça `domain_name` e validação DNS se quiser HTTPS.
- É recomendado criar um pipeline CI para build e push para ECR e então atualizar `var.ecr_image_tag` antes de aplicar.

