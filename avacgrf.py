import pandas as pd
import matplotlib.pyplot as plt
import numpy as np          


class AvocadoStats:

    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    def preprocess_data(self):
        self.data = self.data[['Date', 'AveragePrice']].dropna()
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data = self.data.groupby('Date')['AveragePrice'].mean().reset_index()

    
    def time_series(self):
        # Сортируем по дате
        self.data = self.data.sort_values('Date')

        fig, ax = plt.subplots(figsize=(14, 6))
        fig.patch.set_facecolor('blue')
        ax.set_facecolor('blue')

        # Линия
        ax.plot(
            self.data['Date'], 
            self.data['AveragePrice'],
            color='white', linewidth=2
        )

        ax.xaxis.set_major_locator(plt.MaxNLocator(30))  # ещё больше дат
        ax.tick_params(axis='x', colors='white', rotation=45)

        y_min, y_max = self.data['AveragePrice'].min(), self.data['AveragePrice'].max()
        y_ticks = np.linspace(y_min, y_max, 10)

        for y in y_ticks:
            ax.hlines(
                y,
                xmin=self.data['Date'].min(),
                xmax=self.data['Date'].max(),
                colors='white',
                alpha=0.2,
                linestyles='--'
            )

        ax.set_yticks(y_ticks)
        ax.set_yticklabels([f"{y:.2f}" for y in y_ticks], color='white')

        ax.grid(True, color='white', alpha=0.15, linestyle='--')

        # Заголовки
        ax.set_title('Изменение стоимости авокадо', color='white', fontsize=16)
        ax.set_xlabel('Дата', color='white')
        ax.set_ylabel('Средняя цена (USD)', color='white')

        plt.tight_layout()
        plt.show()


