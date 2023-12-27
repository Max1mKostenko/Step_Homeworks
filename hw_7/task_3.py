text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id quam euismod, gravida metus in, hendrerit sem. 
Sed id justo at neque pharetra consequat. In hac habitasse platea dictumst. 
Integer sed justo ac enim pellentesque malesuada."""

print(sum(1 for i in text if i in [".", "!", "?"]))
