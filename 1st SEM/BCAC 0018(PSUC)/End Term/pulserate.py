import matplotlib.pyplot as plt

def plot_pulse_vs_height():
    num_people = int(input("Enter the number of people: "))
    if num_people <= 0:
        print("Number of people must be positive.")
        return

    heights = []
    pulse_rates = []

    for i in range(num_people):
        height = float(input(f"Enter height for person #{i + 1} (in cm): "))
        pulse_rate = int(input(f"Enter pulse rate for person #{i + 1} (in beats per minute): "))

        heights.append(height)
        pulse_rates.append(pulse_rate)

    # Plotting the graph
    plt.scatter(heights, pulse_rates, marker='o')
    plt.xlabel('Height (cm)')
    plt.ylabel('Pulse Rate (bpm)')
    plt.title('Pulse Rate vs. Height')
    plt.grid(True)
    plt.show()

plot_pulse_vs_height()
