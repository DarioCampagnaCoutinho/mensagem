resource "aws_secretsmanager_secret" "app" {
  name        = "${var.project_name}-secret"
  description = "Secrets for the ${var.project_name} application"
}

resource "aws_secretsmanager_secret_version" "app_version" {
  secret_id = aws_secretsmanager_secret.app.id
  secret_string = jsonencode({
    example_key = "example_value"
  })
}

