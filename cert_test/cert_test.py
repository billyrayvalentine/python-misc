"""A wrapper around Python SSL stdlib for interogating certs"""
import socket
import ssl
from datetime import datetime, timedelta

class Cert:
    """Load a cert from a fqdn with TLS
       NOTE: If the cert is invalid, remaining_days is None"""
    def __init__(self, fqdn, port=443):
        self._cert = None
        self.cert_error = None
        self.is_valid = None
        self.remaining_days = None

        ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
        ssl_socket = ssl_context.wrap_socket(
            socket.socket(socket.AF_INET), server_hostname=fqdn
        )

        try:
            ssl_socket.connect((fqdn, port))
            self._cert = ssl_socket.getpeercert()
        except ssl.CertificateError as e:
            self.is_valid = False
            self.cert_error = e.verify_message
        else:
            self.is_valid = True
            self._calculate_remaining_days()
        finally:
            ssl_socket.close()

    def _calculate_remaining_days(self):
        cert_expiry = ssl.cert_time_to_seconds(self._cert["notAfter"])
        delta = datetime.fromtimestamp(cert_expiry) - datetime.now()
        self.remaining_days = delta.days
