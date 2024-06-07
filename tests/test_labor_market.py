# tests/test_member.py

import unittest
from pimo.labor_market import LaborMarket

class TestLaborMarket(unittest.TestCase):
    def test_matching(self):
        market = LaborMarket(s=1, theta=2.0, sigma=3.0, duration=4.0, size = 10)
        self.assertAlmostEqual(market.matching(), 0.125)  # 2.0 ** -3.0 == 0.125



    def test_find(self):
        market = LaborMarket(s=1, theta=2.0, sigma=3.0, duration=4.0, size = 10)
        self.assertAlmostEqual(market.find(), 0.25)  # 2.0 * 0.125 == 0.25



    def test_generate_trajectory_length(self):
        market = LaborMarket(s=1, theta=2.0, sigma=3.0, duration=40, size = 10)
        # Vérifier si la longueur de la trajectoire générée est égale à la durée spécifiée
        trajectory = market.generate_trajectory()
        assert len(trajectory) == market.duration



    def test_generate_trajectory_values(self):
        market = LaborMarket(s=1, theta=2.0, sigma=3.0, duration=40, size = 10)
        # Vérifier si les valeurs de la trajectoire générée sont correctes (0 pour le chômage, 1 pour l'emploi)
        trajectory = market.generate_trajectory()
        assert all(x == 0 or x == 1 for x in trajectory)



    def test_generate_trajectories(self):
        market = LaborMarket(s=1, theta=2.0, sigma=3.0, duration=40, size = 10)
        market.generate_trajectories()
        trajectories = market.trajectories
        assert(len(trajectories) == market.size)



if __name__ == '__main__':
    unittest.main()
