// Azure SQL Database (mocked)
variable "location" { default = "eastus" }
variable "sql_server_name" { default = "lz-sql-server" }
variable "sql_db_name" { default = "lz-sqldb" }
// This is a placeholder for SQL, as actual deployment requires admin login, etc.
output "sql_server_name" {
  value = var.sql_server_name
}
output "sql_db_name" {
  value = var.sql_db_name
}
