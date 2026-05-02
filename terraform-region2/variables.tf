variable "location" {
  default = "South India"
}

variable "resource_group_name" {
  default = "rg-multiregion-demo-si"
}

variable "aks_name" {
  default = "aks-multiregion-demo-si"
}

variable "acr_name" {
  default = "acrvinaymulti01ci"
}

variable "acr_resource_group_name" {
  default = "rg-multiregion-demo-ci"
}

variable "vm_size" {
  default = "Standard_B2s_v2"
}