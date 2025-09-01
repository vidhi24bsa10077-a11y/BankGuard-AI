/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      // Quantum-themed color palette
      colors: {
        quantum: {
          primary: '#00ff88',     // Bright green - primary quantum color
          secondary: '#0099ff',   // Electric blue - secondary quantum color
          accent: '#8b5cf6',      // Purple - accent color
          danger: '#ff0066',      // Neon red - danger/critical
          warning: '#ffaa00',     // Orange - warnings
          success: '#10b981',     // Green - success states
          info: '#3b82f6',        // Blue - informational
        },
        
        // Custom gray scale for dark theme
        gray: {
          50: '#f9fafb',
          100: '#f3f4f6', 
          200: '#e5e7eb',
          300: '#d1d5db',
          400: '#9ca3af',
          500: '#6b7280',
          600: '#4b5563',
          700: '#374151',
          800: '#1f2937',
          850: '#1a202c',   // Custom darker gray
          900: '#111827',
          950: '#0a0a0a',   // Custom darkest gray
        },
        
        // Threat level colors
        threat: {
          minimal: '#10b981',
          low: '#22c55e', 
          medium: '#eab308',
          high: '#f97316',
          critical: '#ef4444'
        },
        
        // Status colors
        status: {
          clean: '#10b981',
          suspicious: '#eab308', 
          malicious: '#ef4444',
          scanning: '#3b82f6',
          error: '#ef4444'
        }
      },
      
      // Custom fonts
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        mono: ['JetBrains Mono', 'Monaco', 'Menlo', 'Ubuntu Mono', 'monospace'],
        display: ['Inter', 'system-ui', 'sans-serif'],
      },
      
      // Custom font sizes
      fontSize: {
        'xxs': ['0.625rem', { lineHeight: '0.75rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
        '5xl': ['3rem', { lineHeight: '3.5rem' }],
        '6xl': ['3.75rem', { lineHeight: '1' }],
        '7xl': ['4.5rem', { lineHeight: '1' }],
        '8xl': ['6rem', { lineHeight: '1' }],
        '9xl': ['8rem', { lineHeight: '1' }],
      },
      
      // Custom spacing
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '96': '24rem',
        '128': '32rem',
      },
      
      // Custom border radius
      borderRadius: {
        'xl': '0.75rem',
        '2xl': '1rem',
        '3xl': '1.5rem',
        '4xl': '2rem',
      },
      
      // Custom box shadows
      boxShadow: {
        'quantum': '0 0 20px rgba(0, 255, 136, 0.3)',
        'quantum-lg': '0 0 40px rgba(0, 255, 136, 0.4)',
        'quantum-blue': '0 0 20px rgba(0, 153, 255, 0.3)',
        'quantum-purple': '0 0 20px rgba(139, 92, 246, 0.3)',
        'quantum-red': '0 0 20px rgba(255, 0, 102, 0.3)',
        'glow-sm': '0 0 10px rgba(255, 255, 255, 0.1)',
        'glow': '0 0 20px rgba(255, 255, 255, 0.1)',
        'glow-lg': '0 0 40px rgba(255, 255, 255, 0.1)',
        'inner-glow': 'inset 0 0 20px rgba(255, 255, 255, 0.05)',
      },
      
      // Custom animations
      animation: {
        'spin-slow': 'spin 3s linear infinite',
        'pulse-slow': 'pulse 3s infinite',
        'bounce-slow': 'bounce 3s infinite',
        'quantum-pulse': 'quantumPulse 2s infinite',
        'matrix-rain': 'matrixRain 10s linear infinite',
        'scan-line': 'scanLine 2s ease-in-out infinite',
        'glow-pulse': 'glowPulse 2s ease-in-out infinite alternate',
        'float': 'float 6s ease-in-out infinite',
      },
      
      // Custom keyframes
      keyframes: {
        quantumPulse: {
          '0%, 100%': { 
            opacity: '1',
            transform: 'scale(1)',
          },
          '50%': { 
            opacity: '0.7',
            transform: 'scale(1.05)',
            boxShadow: '0 0 30px rgba(0, 255, 136, 0.6)'
          },
        },
        matrixRain: {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100vh)' },
        },
        scanLine: {
          '0%': { 
            transform: 'translateX(-100%)',
            opacity: '0'
          },
          '50%': { 
            opacity: '1'
          },
          '100%': { 
            transform: 'translateX(100%)',
            opacity: '0'
          },
        },
        glowPulse: {
          '0%': { 
            boxShadow: '0 0 5px rgba(0, 255, 136, 0.5)',
          },
          '100%': { 
            boxShadow: '0 0 20px rgba(0, 255, 136, 0.8), 0 0 40px rgba(0, 255, 136, 0.4)',
          },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
      },
      
      // Custom gradients
      backgroundImage: {
        'quantum-gradient': 'linear-gradient(135deg, #00ff88 0%, #0099ff 100%)',
        'quantum-gradient-reverse': 'linear-gradient(135deg, #0099ff 0%, #00ff88 100%)',
        'threat-gradient': 'linear-gradient(135deg, #ef4444 0%, #ff0066 100%)',
        'success-gradient': 'linear-gradient(135deg, #10b981 0%, #22c55e 100%)',
        'warning-gradient': 'linear-gradient(135deg, #eab308 0%, #f59e0b 100%)',
        'grid-pattern': `
          linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px)
        `,
        'quantum-grid': `
          linear-gradient(rgba(0, 255, 136, 0.1) 1px, transparent 1px),
          linear-gradient(90deg, rgba(0, 255, 136, 0.1) 1px, transparent 1px)
        `,
      },
      
      // Custom background sizes
      backgroundSize: {
        'grid-sm': '10px 10px',
        'grid': '20px 20px',
        'grid-lg': '40px 40px',
      },
      
      // Custom z-index scale
      zIndex: {
        '60': '60',
        '70': '70',
        '80': '80',
        '90': '90',
        '100': '100',
      },
      
      // Custom backdrop blur
      backdropBlur: {
        'xs': '2px',
        '3xl': '64px',
      },
      
      // Custom transitions
      transitionTimingFunction: {
        'quantum': 'cubic-bezier(0.4, 0, 0.2, 1)',
        'bounce-in': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
        'ease-out-back': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
      },
      
      // Custom transition durations
      transitionDuration: {
        '2000': '2000ms',
        '3000': '3000ms',
        '4000': '4000ms',
        '5000': '5000ms',
      },
      
      // Screen size extensions for better responsive design
      screens: {
        'xs': '480px',
        '3xl': '1600px',
        '4xl': '1920px',
      },
      
      // Custom aspect ratios
      aspectRatio: {
        'gauge': '1',
        'wide': '16 / 9',
        'cinema': '21 / 9',
      },
      
      // Custom line heights
      lineHeight: {
        '12': '3rem',
        '16': '4rem',
      },
      
      // Custom letter spacing
      letterSpacing: {
        'widest': '0.15em',
      }
    },
  },
  
  // Custom plugins
  plugins: [
    // Custom plugin for quantum-themed utilities
    function({ addUtilities, addComponents, theme }) {
      
      // Quantum glow utilities
      addUtilities({
        '.quantum-glow': {
          boxShadow: '0 0 20px rgba(0, 255, 136, 0.3)',
        },
        '.quantum-glow-strong': {
          boxShadow: '0 0 40px rgba(0, 255, 136, 0.5)',
        },
        '.quantum-glow-blue': {
          boxShadow: '0 0 20px rgba(0, 153, 255, 0.3)',
        },
        '.quantum-glow-red': {
          boxShadow: '0 0 20px rgba(255, 0, 102, 0.3)',
        },
      });
      
      // Quantum text effects
      addUtilities({
        '.text-quantum-glow': {
          textShadow: '0 0 10px rgba(0, 255, 136, 0.8)',
        },
        '.text-glow': {
          textShadow: '0 0 10px rgba(255, 255, 255, 0.5)',
        },
        '.text-matrix': {
          fontFamily: theme('fontFamily.mono'),
          color: theme('colors.quantum.primary'),
          textShadow: '0 0 5px rgba(0, 255, 136, 0.5)',
        },
      });
      
      // Quantum background patterns
      addUtilities({
        '.bg-quantum-grid': {
          backgroundImage: `
            linear-gradient(rgba(0, 255, 136, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 136, 0.1) 1px, transparent 1px)
          `,
          backgroundSize: '20px 20px',
        },
        '.bg-matrix': {
          background: 'radial-gradient(ellipse at center, rgba(0, 255, 136, 0.1) 0%, transparent 70%)',
        },
      });
      
      // Security-themed components
      addComponents({
        '.threat-badge-critical': {
          backgroundColor: theme('colors.threat.critical'),
          color: theme('colors.white'),
          padding: `${theme('spacing.1')} ${theme('spacing.3')}`,
          borderRadius: theme('borderRadius.full'),
          fontSize: theme('fontSize.xs'),
          fontWeight: theme('fontWeight.medium'),
          textTransform: 'uppercase',
        },
        '.threat-badge-high': {
          backgroundColor: theme('colors.threat.high'),
          color: theme('colors.white'),
          padding: `${theme('spacing.1')} ${theme('spacing.3')}`,
          borderRadius: theme('borderRadius.full'),
          fontSize: theme('fontSize.xs'),
          fontWeight: theme('fontWeight.medium'),
          textTransform: 'uppercase',
        },
        '.threat-badge-medium': {
          backgroundColor: theme('colors.threat.medium'),
          color: theme('colors.white'),
          padding: `${theme('spacing.1')} ${theme('spacing.3')}`,
          borderRadius: theme('borderRadius.full'),
          fontSize: theme('fontSize.xs'),
          fontWeight: theme('fontWeight.medium'),
          textTransform: 'uppercase',
        },
        '.threat-badge-low': {
          backgroundColor: theme('colors.threat.low'),
          color: theme('colors.white'),
          padding: `${theme('spacing.1')} ${theme('spacing.3')}`,
          borderRadius: theme('borderRadius.full'),
          fontSize: theme('fontSize.xs'),
          fontWeight: theme('fontWeight.medium'),
          textTransform: 'uppercase',
        },
        '.quantum-card': {
          backgroundColor: theme('colors.gray.800'),
          border: `1px solid ${theme('colors.gray.700')}`,
          borderRadius: theme('borderRadius.xl'),
          padding: theme('spacing.6'),
          transition: 'all 0.3s ease',
          '&:hover': {
            backgroundColor: theme('colors.gray.700'),
            borderColor: theme('colors.gray.600'),
            transform: 'translateY(-2px)',
            boxShadow: '0 10px 30px rgba(0, 0, 0, 0.3)',
          },
        },
        '.quantum-button': {
          background: 'linear-gradient(135deg, #00ff88 0%, #0099ff 100%)',
          color: theme('colors.white'),
          padding: `${theme('spacing.3')} ${theme('spacing.6')}`,
          borderRadius: theme('borderRadius.lg'),
          fontWeight: theme('fontWeight.medium'),
          transition: 'all 0.3s ease',
          border: 'none',
          cursor: 'pointer',
          '&:hover': {
            background: 'linear-gradient(135deg, #00e67a 0%, #0088e6 100%)',
            transform: 'translateY(-1px)',
            boxShadow: '0 0 20px rgba(0, 255, 136, 0.4)',
          },
          '&:active': {
            transform: 'translateY(0)',
          },
        },
      });
      
      // Glass morphism utilities
      addUtilities({
        '.glass': {
          backdropFilter: 'blur(10px)',
          backgroundColor: 'rgba(255, 255, 255, 0.05)',
          border: '1px solid rgba(255, 255, 255, 0.1)',
        },
        '.glass-dark': {
          backdropFilter: 'blur(10px)',
          backgroundColor: 'rgba(0, 0, 0, 0.2)',
          border: '1px solid rgba(255, 255, 255, 0.1)',
        },
        '.glass-quantum': {
          backdropFilter: 'blur(10px)',
          backgroundColor: 'rgba(0, 255, 136, 0.05)',
          border: '1px solid rgba(0, 255, 136, 0.2)',
        },
      });
      
      // Animation utilities
      addUtilities({
        '.animate-scan': {
          animation: 'scanLine 2s ease-in-out infinite',
        },
        '.animate-matrix': {
          animation: 'matrixRain 10s linear infinite',
        },
        '.animate-quantum-pulse': {
          animation: 'quantumPulse 2s infinite',
        },
        '.animate-glow': {
          animation: 'glowPulse 2s ease-in-out infinite alternate',
        },
      });
    },
    
    // Plugin for custom scrollbars
    function({ addUtilities }) {
      addUtilities({
        '.scrollbar-quantum': {
          '&::-webkit-scrollbar': {
            width: '8px',
          },
          '&::-webkit-scrollbar-track': {
            background: '#1f2937',
          },
          '&::-webkit-scrollbar-thumb': {
            background: '#00ff88',
            borderRadius: '4px',
            opacity: '0.7',
          },
          '&::-webkit-scrollbar-thumb:hover': {
            background: '#0099ff',
            opacity: '1',
          },
        },
      });
    },
  ],
  
  // Safelist important classes that might be dynamically generated
  safelist: [
    'text-threat-critical',
    'text-threat-high', 
    'text-threat-medium',
    'text-threat-low',
    'text-threat-minimal',
    'bg-threat-critical',
    'bg-threat-high',
    'bg-threat-medium', 
    'bg-threat-low',
    'bg-threat-minimal',
    'border-threat-critical',
    'border-threat-high',
    'border-threat-medium',
    'border-threat-low',
    'border-threat-minimal',
    'quantum-glow',
    'quantum-glow-blue',
    'quantum-glow-red',
    'animate-quantum-pulse',
    'animate-glow',
  ],
};
