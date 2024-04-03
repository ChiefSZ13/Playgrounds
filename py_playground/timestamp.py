import time

def get_current_timestamp_ms():
    return int(time.time() * 1000)

# Example usage
current_timestamp_ms = get_current_timestamp_ms()
print(f"Current UNIX timestamp in milliseconds: {current_timestamp_ms}")
