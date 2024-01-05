import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 10, 1000)

def normal_oscillation(frequency, phase_shift):
    trajectory = np.cos(frequency*time - phase_shift)
    
    return trajectory


def damped_oscillation(frequency, phase_shift, damping_coefficient):
    damped_frequency = np.sqrt(damping_coefficient**2 - frequency**2)
    trajectory = np.exp(-damping_coefficient*time)*(np.exp(damped_frequency*time - phase_shift) + np.exp(-damped_frequency*time - phase_shift))
    
    return trajectory


def save_normal_plot(frequency, phase_shift):
    x_t = normal_oscillation(frequency, phase_shift)
    
    plt.plot(time, x_t)
    plt.savefig('./Plots/normal_oscillation.png')

def save_damped_plot(frequency, phase_shift, damping_coefficient):
    
    x_t = damped_oscillation(frequency, phase_shift)
        
    plt.plot(time, x_t)
    plt.savefig('./Plots/damped_oscillation.png')