# eureka-ansible-inventory

Creates an ansible inventory base on Eureka registered hosts.

# How to install

Just install using:
```
pip install git+ssh://git@github.com/padilo/eureka-ansible-inventory.git
```
# How to use

Define an environment variable EUREKA_HOST with just hostname[:port]. For instance:
```
export EUREKA_HOST=eureka.host:8080
```

With environment variable defined you can use it as follows:
```
ansible MY_EUREKA_CLIENT -i $(eureka-inventory-get) -m debug
```
