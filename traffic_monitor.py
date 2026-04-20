from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer

log = core.getLogger()

packet_count = 0
byte_count = 0

def _handle_PacketIn(event):
    global packet_count, byte_count

    packet_count += 1
    byte_count += len(event.ofp.data)

    packet = event.parsed

    if packet.find('ipv4'):
        ip = packet.find('ipv4')

        # 🚫 BLOCK traffic from h1
        if str(ip.srcip) == "10.0.0.1":
            log.info("🚫 Blocked traffic from h1")

            msg = of.ofp_flow_mod()
            msg.match = of.ofp_match.from_packet(packet)
            event.connection.send(msg)

            return

    # ✅ Normal forwarding
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)


def print_stats():
    log.info(f"📊 REPORT → Packets: {packet_count} | Bytes: {byte_count}")


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    Timer(5, print_stats, recurring=True)

    log.info("Traffic Monitor Controller Started 🚀")
