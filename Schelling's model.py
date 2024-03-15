import numpy as np
import matplotlib.pyplot as plt

# Parameters
grid_size = 20  # Size of the grid
num_agents = 100  # Number of agents
similarity_threshold = 0.5  # Similarity threshold for preference
num_iterations = 100  # Number of simulation iterations

# Initialize grid
grid = np.zeros((grid_size, grid_size))

# Place agents randomly on the grid
agent_positions = np.random.randint(0, grid_size, size=(num_agents, 2))
agent_colors = np.random.randint(0, 2, size=num_agents)  # Random colors for agents

# Function to calculate similarity between agents
def calculate_similarity(agent_color, neighbor_color):
    return agent_color == neighbor_color

# Main simulation loop
for _ in range(num_iterations):
    # Shuffle agent positions for random order of movement
    np.random.shuffle(agent_positions)
    
    # Move agents based on preference
    for agent_idx, (agent_row, agent_col) in enumerate(agent_positions):
        similar_neighbors = 0
        total_neighbors = 0
        
        # Count similar neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip agent itself
                neighbor_row = (agent_row + dr) % grid_size
                neighbor_col = (agent_col + dc) % grid_size
                if grid[neighbor_row, neighbor_col] == agent_colors[agent_idx]:
                    similar_neighbors += 1
                total_neighbors += 1
        
        # Check if agent is dissatisfied
        similarity_ratio = similar_neighbors / total_neighbors
        if similarity_ratio < similarity_threshold:
            # Move agent to a random empty cell
            empty_cells = np.argwhere(grid == 0)
            if len(empty_cells) > 0:
                new_position = empty_cells[np.random.randint(len(empty_cells))]
                grid[new_position[0], new_position[1]] = agent_colors[agent_idx]
                grid[agent_row, agent_col] = 0

# Visualize final grid
plt.imshow(grid, cmap='gray')
plt.title("Simulation of Visual Segregation")
plt.axis('off')
plt.show()

