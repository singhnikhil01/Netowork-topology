import subprocess
import time

def collect_throughput(server_host, client_host, duration=10):
    """
    Collect throughput data between a server and a client using iperf3.

    Args:
        server_host (str): The IP address of the server host.
        client_host (str): The IP address of the client host.
        duration (int, optional): The duration of the iperf3 test in seconds. Defaults to 10.

    Returns:
        tuple: A tuple containing the iperf3 output and error.
    """

    try:
        # Start iperf3 server in the background
        print("Starting iperf3 server...")
        server_process = subprocess.Popen(['iperf3', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("iperf3 server started.")

        # Wait for a moment to ensure the server is ready
        time.sleep(2)

        # Start iperf3 client
        print("Starting iperf3 client...")
        client_process = subprocess.Popen(['iperf3', '-c', server_host, '-t', str(duration)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("iperf3 client started.")

        # Wait for the client process to complete
        client_output, client_error = client_process.communicate()

        # Print the client output and error
        print("Client Output:", client_output.decode())
        print("Client Error:", client_error.decode())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Terminate the iperf3 server process
        server_process.terminate()
        print("iperf3 server terminated.")

    return client_output, client_error

if __name__ == '__main__':
    server_host = '10.0.0.1'  # Replace with the actual IP address of h1
    client_host = '10.0.0.2'  # Replace with the actual IP address of h2
    collect_throughput(server_host, client_host)