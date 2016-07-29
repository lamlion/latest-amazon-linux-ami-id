# Fetch Amazon Linux AMI IDs from web
Why? Because ec2 describe-images API is sub-par.
You almost always want HVM (SSD) EBS-Backed 64-bit.

Partial output example:
```
{
    "China Beijing": {
        "HVM (NAT) EBS-Backed 64-bit": "ami-7b549e16",
        "PV EBS-Backed 64-bit": "ami-77559f1a",
        "HVM Instance Store 64-bit": "ami-1d6ba170",
        "PV Instance Store 64-bit": "ami-73569c1e",
        "HVM (SSD) EBS-Backed 64-bit": "ami-8e6aa0e3",
        "HVM (Graphics) EBS-Backed 64-bit": "n/a"
    },
    "EU Ireland": {
        "HVM (NAT) EBS-Backed 64-bit": "ami-a8dd45db",
        "PV EBS-Backed 64-bit": "ami-4cdd453f",
        "HVM Instance Store 64-bit": "ami-e9d9419a",
        "PV Instance Store 64-bit": "ami-42df4731",
        "HVM (SSD) EBS-Backed 64-bit": "ami-f9dd458a",
        "HVM (Graphics) EBS-Backed 64-bit": "AWS Marketplace"
    }
}
```
