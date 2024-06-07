# your_module/member.py
import random
import numpy as np

class LaborMarket:
    def __init__(self, s, theta, sigma, duration, size):
        self.s = s
        self.theta = theta
        self.sigma = sigma
        self.duration = duration
        self.size = size
        self.trajectories = None



    def matching(self):
        """
        Calcule le flux de probabilité d'un match
        """
        return self.theta ** (-self.sigma)



    def find(self):
        """
        Calcule le flux de probabilité de trouver un travail
        """
        return self.theta * self.matching()



    def generate_trajectory(self):
        """
        Generate a random trajectory of labor market status (0 for unemployed, 1 for employed).

        Args:
            labor_market (LaborMarket): Instance of LaborMarket class.
            steps (int): Number of steps in the trajectory.

        Returns:
            list: List representing the trajectory.
        """
        trajectory = [0]  # Start with unemployed
        for _ in range(self.duration - 1):
            if trajectory[-1] == 0:  # If unemployed
                if random.random() < self.find():
                    trajectory.append(1)  # Employed
                else:
                    trajectory.append(0)  # Remain unemployed
            else:  # If employed
                if random.random() < self.s:
                    trajectory.append(0)  # Job destruction
                else:
                    trajectory.append(1)  # Remain employed
        return trajectory
    
    

    def generate_trajectories(self):
        """
        Generate the trajectories for each member and sets the attribute trajectories
        """
        trajectories = []
        for _ in range(self.size):
            trajectory = self.generate_trajectory()
            trajectories.append(trajectory)
        self.trajectories = trajectories


