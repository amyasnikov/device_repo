__all__ = ['vrrp_config']

def vrrp_config(device):
    return jq(
        "[[(.interfaces[] | select(.vrrp)).interface],[(.interfaces[] | select(.vrrp)).vrrp]] | transpose | map( {(.[0]): .[1]})",
        device.config
    )
