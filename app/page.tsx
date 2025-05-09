'use client';

import { useState } from 'react';
import { 
  Container, 
  Box, 
  Typography, 
  Button, 
  Paper,
  CircularProgress
} from '@mui/material';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise'];

export default function Home() {
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [predictions, setPredictions] = useState<number[] | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleImageUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    setLoading(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('image', file);

      // Create a preview URL for the image
      const previewUrl = URL.createObjectURL(file);
      setSelectedImage(previewUrl);

      // In a real deployment, this would be your API endpoint
      // For now, we'll simulate a response
      const mockPredictions = emotions.map(() => Math.random());
      setPredictions(mockPredictions);
    } catch (err) {
      setError('Error processing image. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const chartData = {
    labels: emotions,
    datasets: [
      {
        label: 'Emotion Probabilities',
        data: predictions || emotions.map(() => 0),
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top' as const,
      },
      title: {
        display: true,
        text: 'Emotion Probabilities',
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 1,
      },
    },
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          Facial Emotion Recognition
        </Typography>
        
        <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
          <Box sx={{ textAlign: 'center', mb: 2 }}>
            <input
              accept="image/*"
              style={{ display: 'none' }}
              id="image-upload"
              type="file"
              onChange={handleImageUpload}
            />
            <label htmlFor="image-upload">
              <Button
                variant="contained"
                component="span"
                disabled={loading}
              >
                Upload Image
              </Button>
            </label>
          </Box>

          {loading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', my: 2 }}>
              <CircularProgress />
            </Box>
          )}

          {error && (
            <Typography color="error" align="center">
              {error}
            </Typography>
          )}

          {selectedImage && (
            <Box sx={{ textAlign: 'center', my: 2 }}>
              <img
                src={selectedImage}
                alt="Uploaded"
                style={{ maxWidth: '100%', maxHeight: '300px' }}
              />
            </Box>
          )}

          {predictions && (
            <Box sx={{ mt: 3 }}>
              <Typography variant="h6" gutterBottom>
                Predicted Emotion: {emotions[predictions.indexOf(Math.max(...predictions))].toUpperCase()}
              </Typography>
              <Bar data={chartData} options={chartOptions} />
            </Box>
          )}
        </Paper>
      </Box>
    </Container>
  );
}
