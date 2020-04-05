import subprocess
import socket
import time
import pytest

@pytest.fixture(scope="session")
# setting scope to be session means this fixture initialized only once and terminated at end of test session
def echoserver():
	print("Loading server")
	p = subprocess.Popen(["python", "echo_server.py"])
	time.sleep(1)
	yield p
	p.terminate()

# decorator without options means that a new socket object instantiated for each test
@pytest.fixture
def clientsocket(request):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("localhost", 1028))
	yield s
	s.close()

def test_echo(echoserver, clientsocket):
	clientsocket.send(b"abc")
	assert clientsocket.recv(3) == b"abc"

def test_echo2(echoserver, clientsocket):
	clientsocket.send(b"def")
	assert clientsocket.recv(3) == b"def"