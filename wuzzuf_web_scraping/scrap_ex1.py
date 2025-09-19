
import scrap_helper

# Get the data
data, df = scrap_helper.scrap_pages('python developer')

# Save the data
df.to_csv('data.csv', index=False)

if __name__ == '__main__':
    print('Done')