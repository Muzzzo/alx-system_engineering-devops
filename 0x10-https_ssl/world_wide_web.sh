#!/bin/bash

# Function to display information about a specific subdomain
get_subdomain_info() {
    local subdomain=$1
    local domain=$2
    dig_output=$(dig ${subdomain}.${domain} | awk '/ANSWER SECTION/ { getline; print $4 }')
    record_type=$(echo $dig_output | awk '{print $2}')
    destination=$(echo $dig_output | awk '{print $1}')
    echo "The subdomain ${subdomain} is a ${record_type} record and points to ${destination}"
}

# Function to display information about default subdomains
get_default_subdomains_info() {
    local domain=$1
    subdomains=("www" "lb-01" "web-01" "web-02")
    for subdomain in "${subdomains[@]}"; do
        get_subdomain_info ${subdomain} ${domain}
    done
}

# Main script
if [ $# -eq 1 ]; then
    domain=$1
    get_default_subdomains_info ${domain}
elif [ $# -eq 2 ]; then
    domain=$1
    subdomain=$2
    get_subdomain_info ${subdomain} ${domain}
else
    echo "Usage: $0 domain [subdomain]"
    exit 1
fi
