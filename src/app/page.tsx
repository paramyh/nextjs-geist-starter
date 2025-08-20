'use client'

import { useState } from 'react'

export default function Home() {
  const [activeSection, setActiveSection] = useState('hero')

  return (
    <div className="min-h-screen bg-white text-black">
      {/* Navigation */}
      <nav className="fixed top-0 w-full bg-white/90 backdrop-blur-sm border-b border-gray-100 z-50">
        <div className="max-w-6xl mx-auto px-6 py-4">
          <div className="flex justify-between items-center">
            <div className="text-2xl font-bold tracking-tight">Minimal</div>
            <div className="hidden md:flex space-x-8">
              <button 
                onClick={() => setActiveSection('hero')}
                className="text-sm font-medium hover:text-gray-600 transition-colors"
              >
                Home
              </button>
              <button 
                onClick={() => setActiveSection('about')}
                className="text-sm font-medium hover:text-gray-600 transition-colors"
              >
                About
              </button>
              <button 
                onClick={() => setActiveSection('contact')}
                className="text-sm font-medium hover:text-gray-600 transition-colors"
              >
                Contact
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="min-h-screen flex items-center justify-center px-6">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-6xl md:text-8xl font-bold tracking-tighter mb-6">
            Less is
            <br />
            <span className="text-gray-400">More</span>
          </h1>
          <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-2xl mx-auto">
            A modern approach to digital minimalism through clean design and intentional functionality.
          </p>
          <button className="px-8 py-4 bg-black text-white font-medium hover:bg-gray-800 transition-colors">
            Explore
          </button>
        </div>
      </section>

      {/* About Section */}
      <section className="min-h-screen flex items-center justify-center px-6 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-4xl md:text-5xl font-bold tracking-tighter mb-6">
                Purposeful
                <br />
                Design
              </h2>
              <p className="text-lg text-gray-600 mb-4">
                Every element serves a function. Every space has intention. We believe in creating experiences that respect both the user and the medium.
              </p>
              <p className="text-lg text-gray-600">
                Through restraint and careful consideration, we achieve clarity that transcends trends.
              </p>
            </div>
            <div className="space-y-4">
              <div className="border border-gray-200 p-6">
                <div className="text-sm font-medium text-gray-500 mb-2">01</div>
                <div className="text-lg font-medium">Clarity</div>
              </div>
              <div className="border border-gray-200 p-6">
                <div className="text-sm font-medium text-gray-500 mb-2">02</div>
                <div className="text-lg font-medium">Function</div>
              </div>
              <div className="border border-gray-200 p-6">
                <div className="text-sm font-medium text-gray-500 mb-2">03</div>
                <div className="text-lg font-medium">Balance</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="min-h-screen flex items-center justify-center px-6">
        <div className="max-w-2xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold tracking-tighter mb-6">
            Let's Create
            <br />
            Together
          </h2>
          <p className="text-lg text-gray-600 mb-8">
            Ready to bring clarity to your next project? We'd love to hear from you.
          </p>
          <div className="space-y-4">
            <input 
              type="email" 
              placeholder="your@email.com"
              className="w-full px-6 py-4 border border-gray-200 focus:outline-none focus:border-black transition-colors"
            />
            <textarea 
              placeholder="Tell us about your project..."
              rows={4}
              className="w-full px-6 py-4 border border-gray-200 focus:outline-none focus:border-black transition-colors resize-none"
            />
            <button className="w-full px-8 py-4 bg-black text-white font-medium hover:bg-gray-800 transition-colors">
              Send Message
            </button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-100 py-12">
        <div className="max-w-6xl mx-auto px-6">
          <div className="flex justify-between items-center">
            <div className="text-sm text-gray-600">© 2024 Minimal. All rights reserved.</div>
            <div className="flex space-x-6">
              <a href="#" className="text-sm text-gray-600 hover:text-black transition-colors">Privacy</a>
              <a href="#" className="text-sm text-gray-600 hover:text-black transition-colors">Terms</a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
