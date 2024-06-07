# visualize/visualize.py
import plotly.graph_objects as go

class Visualize:
    def plot_line_chart(self, x_data, y_data, title="Line Chart", x_label="X", y_label="Y"):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines', name='Line'))
        fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
        fig.show()



    def plot_bar_chart(self, x_data, y_data, title="Bar Chart", x_label="X", y_label="Y"):
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x_data, y=y_data, name='Bar'))
        fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
        fig.show()



    def plot_scatter_chart(self, x_data, y_data, title="Scatter Plot", x_label="X", y_label="Y"):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='markers', name='Scatter'))
        fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
        fig.show()



    def plot_trajectory(self, trajectory):
        """
        Trace la trajectoire.

        Args:
            trajectory (list): Liste représentant la trajectoire.
        """
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=trajectory, mode='markers', name='Trajectory'))
        fig.update_layout(title="Employment Trajectory", xaxis_title="Time", yaxis_title="Employment Status")
        fig.show()



    def plot_trajectories(self, trajectories):
        """
        Trace la trajectoire.

        Args:
            trajectory (list): Liste représentant la trajectoire.
        """
        fig = go.Figure()
        for trajectory in trajectories:
            fig.add_trace(go.Scatter(y=trajectory, mode='lines'))
        fig.update_layout(title="Employment Trajectories", xaxis_title="Time", yaxis_title="Employment Status")
        fig.show()

