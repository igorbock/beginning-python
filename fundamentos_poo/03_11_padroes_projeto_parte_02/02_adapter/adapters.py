from interfaces import DataProcessor, DataVisualizer
from legacy_system import LegacyDataAnalyzer, LegacyChartGenerator


class LegacyDataAnalyzerAdapter(DataProcessor):
    """Adapter for LegacyDataAnalyzer to work with the DataProcessor interface."""

    def __init__(self):
        self.legacy_analyzer = LegacyDataAnalyzer()

    def _validate_numeric_list(self, data):
        if not isinstance(data, list):
            raise ValueError("Data must be a list of numeric values")
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("All data items must be numeric")

    def process_data(self, data):
        """Process data using the legacy analyzer."""
        self._validate_numeric_list(data)

        # Legacy espera que load_data receba a lista
        self.legacy_analyzer.load_data(data)

        # run_analysis retorna True/False dependendo do cenário legado
        return self.legacy_analyzer.run_analysis()

    def get_results(self):
        """Get results from the legacy analyzer."""
        results = self.legacy_analyzer.fetch_results()
        return {} if results is None else results


class LegacyChartGeneratorAdapter(DataVisualizer):
    """Adapter for LegacyChartGenerator to work with the DataVisualizer interface."""

    def __init__(self, chart_type="bar"):
        self.chart_type = chart_type
        self.legacy_chart_generator = LegacyChartGenerator()
        self.legacy_chart_generator.initialize_chart(self.chart_type)

    def _validate_numeric_list(self, data):
        if not isinstance(data, list):
            raise ValueError("Data must be a list of numeric values")
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("All data items must be numeric")

    def visualize(self, data):
        """Create visualization using the legacy chart generator."""
        self._validate_numeric_list(data)

        # Legacy espera que add_data_series receba a lista
        self.legacy_chart_generator.add_data_series(data)
        return self.legacy_chart_generator.render()

    def export_visualization(self, filename):
        """Export the visualization to a file using the legacy chart generator."""
        if not isinstance(filename, str):
            filename = str(filename)

        if not filename.lower().endswith((".png", ".jpg", ".pdf")):
            filename += ".png"

        return self.legacy_chart_generator.save_chart(filename)