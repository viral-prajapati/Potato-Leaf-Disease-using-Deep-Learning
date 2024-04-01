import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  // Render the App component
  render(<App />);
  
  // Find an element with text matching the regular expression /learn react/i
  const linkElement = screen.getByText(/learn react/i);
  
  // Assert that the found element is in the document
  expect(linkElement).toBeInTheDocument();
});
