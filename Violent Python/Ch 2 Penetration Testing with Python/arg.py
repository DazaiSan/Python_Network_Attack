import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--H', dest = "host",type=str,help = "specify target host")
parser.add_argument('--p', dest = "ports",nargs = '+' ,type=str,help = "specify ports separated by space")
args = parser.parse_args()
host = args.host
portlist = args.ports
print(parser.print_help())
print(host,portlist)