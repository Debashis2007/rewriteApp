import { useState } from 'react';
import { Copy, RefreshCw, Zap, MessageSquare } from 'lucide-react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const styles = {
  container: {
    minHeight: '100vh',
    width: '100%',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    padding: '24px',
    display: 'flex',
    flexDirection: 'column',
  },
  content: {
    width: '100%',
    flex: 1,
    background: 'white',
    borderRadius: '12px',
    boxShadow: '0 20px 60px rgba(0, 0, 0, 0.3)',
    padding: '32px',
  },
  header: {
    textAlign: 'center',
    marginBottom: '30px',
  },
  title: {
    fontSize: '28px',
    fontWeight: 'bold',
    color: '#667eea',
    margin: '0 0 8px 0',
  },
  subtitle: {
    color: '#666',
    fontSize: '14px',
    margin: '0',
  },
  gridContainer: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
    gap: '20px',
    marginBottom: '20px',
  },
  panel: {
    background: '#fff',
    border: '2px solid #e0e0e0',
    borderRadius: '8px',
    padding: '20px',
  },
  label: {
    fontWeight: '600',
    marginBottom: '8px',
    color: '#333',
    fontSize: '14px',
    display: 'block',
  },
  textarea: {
    width: '100%',
    minHeight: '300px',
    padding: '15px',
    border: '2px solid #e0e0e0',
    borderRadius: '8px',
    fontFamily: 'monospace',
    fontSize: '14px',
    lineHeight: '1.6',
    resize: 'vertical',
  },
  charCount: {
    marginTop: '8px',
    fontSize: '12px',
    color: '#999',
  },
  buttonGroup: {
    display: 'flex',
    gap: '12px',
    marginTop: '12px',
    flexWrap: 'wrap',
  },
  button: {
    padding: '10px 20px',
    border: 'none',
    borderRadius: '8px',
    fontWeight: '600',
    fontSize: '14px',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    transition: 'all 0.2s',
  },
  buttonPrimary: {
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: 'white',
  },
  buttonSecondary: {
    background: '#f5f5f5',
    color: '#333',
    border: '1px solid #e0e0e0',
  },
  controlsPanel: {
    background: '#f9f9f9',
    border: '2px solid #e0e0e0',
    borderRadius: '8px',
    padding: '20px',
    marginBottom: '20px',
  },
  controlsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
    gap: '20px',
  },
  select: {
    width: '100%',
    padding: '10px 12px',
    border: '2px solid #e0e0e0',
    borderRadius: '8px',
    fontSize: '14px',
    backgroundColor: 'white',
    cursor: 'pointer',
  },
  error: {
    background: '#fee',
    border: '1px solid #fcc',
    color: '#c33',
    padding: '12px 16px',
    borderRadius: '8px',
    marginTop: '20px',
    fontSize: '14px',
  },
  analysisPanel: {
    background: '#f9f9f9',
    border: '2px solid #e0e0e0',
    borderRadius: '8px',
    padding: '20px',
    marginTop: '20px',
  },
  analysisTitle: {
    fontWeight: '600',
    marginBottom: '15px',
    color: '#333',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
  },
  metricsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(120px, 1fr))',
    gap: '15px',
  },
  metric: {
    background: 'white',
    padding: '12px',
    borderRadius: '6px',
    borderLeft: '4px solid #667eea',
  },
  metricLabel: {
    fontSize: '12px',
    color: '#999',
    textTransform: 'uppercase',
    marginBottom: '4px',
  },
  metricValue: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#667eea',
  },
};

export default function App() {
  const [originalText, setOriginalText] = useState('');
  const [rewrittenText, setRewrittenText] = useState('');
  const [tone, setTone] = useState('formal');
  const [action, setAction] = useState('rewrite');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [analysis, setAnalysis] = useState(null);

  const handleRewrite = async () => {
    if (!originalText.trim()) {
      setError('Please enter some text to rewrite');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post(`${API_BASE_URL}/rewrite`, {
        text: originalText,
        tone,
        action,
      });

      setRewrittenText(response.data.rewritten);
      setAnalysis(response.data.analysis);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to rewrite text');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(rewrittenText);
  };

  const handleSwap = () => {
    setOriginalText(rewrittenText);
    setRewrittenText('');
  };

  const handleClear = () => {
    setOriginalText('');
    setRewrittenText('');
    setError('');
    setAnalysis(null);
  };

  return (
    <div style={styles.container}>
      <div style={styles.content}>
        {/* Header */}
        <div style={styles.header}>
          <h1 style={styles.title}>Rewrite Professional</h1>
          <p style={styles.subtitle}>Transform your text with AI-powered rewriting</p>
        </div>

        {/* Text Panels */}
        <div style={styles.gridContainer}>
          {/* Original Text */}
          <div style={styles.panel}>
            <label style={styles.label}>Original Text</label>
            <textarea
              value={originalText}
              onChange={(e) => setOriginalText(e.target.value)}
              placeholder="Paste your text here..."
              style={styles.textarea}
            />
            <div style={styles.charCount}>{originalText.length} characters</div>
          </div>

          {/* Rewritten Text */}
          <div style={styles.panel}>
            <label style={styles.label}>Rewritten Text</label>
            <textarea
              value={rewrittenText}
              readOnly
              placeholder="Your rewritten text will appear here..."
              style={{ ...styles.textarea, backgroundColor: '#f9f9f9' }}
            />
            <div style={styles.buttonGroup}>
              <button
                onClick={handleCopy}
                disabled={!rewrittenText}
                style={{
                  ...styles.button,
                  ...styles.buttonPrimary,
                  opacity: !rewrittenText ? 0.6 : 1,
                  cursor: !rewrittenText ? 'not-allowed' : 'pointer',
                }}
              >
                <Copy size={16} /> Copy
              </button>
              <button
                onClick={handleSwap}
                disabled={!rewrittenText}
                style={{
                  ...styles.button,
                  ...styles.buttonSecondary,
                  opacity: !rewrittenText ? 0.6 : 1,
                  cursor: !rewrittenText ? 'not-allowed' : 'pointer',
                }}
              >
                <RefreshCw size={16} /> Swap
              </button>
            </div>
          </div>
        </div>

        {/* Controls */}
        <div style={styles.controlsPanel}>
          <div style={styles.controlsGrid}>
            {/* Tone */}
            <div>
              <label style={styles.label}>Tone</label>
              <select
                value={tone}
                onChange={(e) => setTone(e.target.value)}
                style={styles.select}
              >
                <option value="formal">Formal</option>
                <option value="friendly">Friendly</option>
                <option value="assertive">Assertive</option>
              </select>
            </div>

            {/* Action */}
            <div>
              <label style={styles.label}>Action</label>
              <select
                value={action}
                onChange={(e) => setAction(e.target.value)}
                style={styles.select}
              >
                <option value="rewrite">Rewrite</option>
                <option value="shorten">Shorten</option>
                <option value="strengthen">Strengthen</option>
              </select>
            </div>

            {/* Buttons */}
            <div style={{ display: 'flex', gap: '12px', alignItems: 'flex-end' }}>
              <button
                onClick={handleRewrite}
                disabled={loading}
                style={{
                  ...styles.button,
                  ...styles.buttonPrimary,
                  flex: 1,
                  justifyContent: 'center',
                  opacity: loading ? 0.6 : 1,
                  cursor: loading ? 'not-allowed' : 'pointer',
                }}
              >
                <Zap size={18} />
                {loading ? 'Processing...' : 'Rewrite'}
              </button>
              <button
                onClick={handleClear}
                style={{
                  ...styles.button,
                  ...styles.buttonSecondary,
                  flex: 1,
                  justifyContent: 'center',
                }}
              >
                Clear
              </button>
            </div>
          </div>
        </div>

        {/* Error */}
        {error && <div style={styles.error}>{error}</div>}

        {/* Analysis */}
        {analysis && (
          <div style={styles.analysisPanel}>
            <h2 style={styles.analysisTitle}>
              <MessageSquare size={20} /> Text Analysis
            </h2>
            <div style={styles.metricsGrid}>
              <div style={styles.metric}>
                <div style={styles.metricLabel}>Words</div>
                <div style={styles.metricValue}>{analysis.word_count}</div>
              </div>
              <div style={styles.metric}>
                <div style={styles.metricLabel}>Characters</div>
                <div style={styles.metricValue}>{analysis.char_count}</div>
              </div>
              <div style={styles.metric}>
                <div style={styles.metricLabel}>Sentences</div>
                <div style={styles.metricValue}>{analysis.sentence_count}</div>
              </div>
              <div style={styles.metric}>
                <div style={styles.metricLabel}>Avg Word Length</div>
                <div style={styles.metricValue}>{analysis.avg_word_length.toFixed(1)}</div>
              </div>
              <div style={styles.metric}>
                <div style={styles.metricLabel}>Detected Tone</div>
                <div style={{ ...styles.metricValue, textTransform: 'capitalize' }}>
                  {analysis.tone_detected}
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
