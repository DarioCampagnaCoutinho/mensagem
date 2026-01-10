# ACM Certificate resource (commented by default). To enable, set var.enable_acm = true and uncomment the resource.

# resource "aws_acm_certificate" "app" {
#   domain_name       = "example.com"
#   validation_method = "DNS"
#
#   tags = {
#     Name = "${var.project_name}-acm"
#   }
# }
#
# If using DNS validation, add aws_route53_record resources to complete validation.

