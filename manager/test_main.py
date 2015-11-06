import sys
# from fqsocks import config_file
import shell
import config
from fqsocks import fqsocks
from fqsocks.fqsocks import main

# config_file.cli_args =

args = [
    '--log-level', 'INFO',
    '--log-file', '/data/data/fq.router2/log/fqsocks.log',
    '--ifconfig-command', '/data/data/fq.router2/busybox',
    '--ip-command', '/data/data/fq.router2/busybox',
    '--outbound-ip', '10.1.2.3',
    '--tcp-gateway-listen', '10.1.2.3:12345',
    '--dns-server-listen', '10.1.2.3:12345']
if shell.USE_SU:
    args.append('--no-tcp-scrambler')
args = config.configure_fqsocks(args)
fqsocks.init_config(args)

main()
